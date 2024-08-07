"""
The baci class and main cli
"""

import sys
import os
from argparse import ArgumentParser
from typing import Iterable

from baci.formatters import BaciHelpFormatter
from baci.repositories.make_command import make_command


def normalize_argv(argv):
    if argv is None:
        return sys.argv

    script = os.path.basename(__file__)
    try:
        i = argv.index(script)
    except ValueError:
        return argv
    return " ".join(argv[: i + 1]) + argv[i + 1 :]


def get_exe():
    """
    Gets a potentially shortend name of the executable
    running the prog
    """
    exe = sys.executable
    if not exe:
        return sys.argv[0] if len(sys.argv) > 0 else ""

    if "/" in exe:
        # it might be a path
        PATH = os.environ.get("PATH", "").split(":")
        if os.path.dirname(exe) in PATH:
            # executable can be ran as its single name rather
            # than the full path
            return os.path.basename(exe)

        cwd = os.getcwd()
        relpath = os.path.relpath(exe, cwd)
        if ".." not in relpath:
            return relpath

    return exe


class Baci:

    def __init__(self, prog=None, commands: Iterable[callable] = None, _print=print):
        self.commands: Iterable[callable] = commands or tuple()
        self.prog = " ".join([get_exe(), sys.argv[0]]) if prog is None else prog
        self._print = _print

    def run(self, argv=None):

        # TODO top-level command
        parser = ArgumentParser(self.prog, description="TODO", formatter_class=BaciHelpFormatter)
        subparsers = parser.add_subparsers(dest="command")

        command_lookup = {}
        for rawcommand in self.commands:
            command = make_command(rawcommand)
            subparser = subparsers.add_parser(command.name, formatter_class=BaciHelpFormatter)
            command.parse_with(subparser, argv)
            command_lookup[command.name] = command

        if argv is None:
            argv = sys.argv[1:]
        parsed = parser.parse_args(argv)

        if parsed.command in command_lookup:
            baci_command = command_lookup[parsed.command]
            baci_command.run(parsed)
            return

        # print help if no command found
        parser.print_usage()
