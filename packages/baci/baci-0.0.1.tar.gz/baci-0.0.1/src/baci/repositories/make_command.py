import inspect

from baci.factories.command import _argument_from_param, ARGUMENT, Command


def make_command(fn):
    """
    Makes a command out of a function
    """
    parameters = inspect.signature(fn).parameters
    posargs, flags = make_arguments(parameters)

    return Command(fn.__name__, fn, flags=flags, arguments=posargs)


def make_arguments(parameters):
    """
    Makes arguments out of parameters,
    usually from inspect.signature().parameters
    """
    posargs = []
    flags = {}
    for p in parameters.values():
        args = _argument_from_param(p)
        for arg in args:
            if arg.kind == ARGUMENT:
                posargs.append(arg)
            else:
                flags[arg.name] = arg

    return posargs, flags
