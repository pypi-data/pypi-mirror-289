from typing import Dict, List

from baci.actions import CountOrValueAction, ParseOptionalFlag
from baci.util import to_snake_case

ANY = object()


class ArgParseError(Exception):
    pass


class BaseArgv:
    pass


ARGUMENT = "ARGUMENT"
FLAG_SHORT = "FLAG_SHORT"
FLAG_LONG = "FLAG_LONG"

NO_DEFAULT = object()


class Argument(BaseArgv):
    """
    Argument class
    NOTE: types are *weak*, only validators return errors. casts return None if the type cant be parsed
    """

    def __init__(
        self,
        description,
        kind,
        required: bool = None,
        name: str = None,
        type=ANY,
        check=None,
        default=NO_DEFAULT,
    ):

        if kind in (FLAG_SHORT, FLAG_LONG):
            required = False if required is None else required
            default = None if default is NO_DEFAULT else default
            type = bool if type is ANY else type
        else:
            if default is not NO_DEFAULT and required is None:
                required = False
            elif default is NO_DEFAULT and required is False:
                default = None

        self.name = name
        self.type = type
        self.validators = check
        self.description = description
        self.default = default
        self.kind = kind
        self.required = required

    def get_data(self):
        return {
            "name": self.name,
            "default": self.default,
            "description": self.description,
            "validators": self.validators or [],
        }

    def parse(self, arg):
        """
        validates and parses argument for passing to handler
        """
        if arg is None:
            if arg.default is None:
                return ArgParseError("Required")
            return arg.default

        if self.type is ANY:
            return arg
        if self.type in (int, str):
            try:
                return self.type(arg)
            except:
                return None
        raise NotImplementedError("error about bad config annotation")


class Command:

    def __init__(
        self,
        name,
        handler,
        description="",
        flags: Dict[str, Argument] = None,
        arguments: List[Argument] = None,
    ):
        self.name = to_snake_case(name)
        self.description = description
        self.flags = flags or {}
        self.arguments = arguments or []
        self.handler = handler

    def run(self, namespace):
        args = [getattr(namespace, a.name, a.default) for a in self.arguments]
        kwargs = { a.name: getattr(namespace, a.name, a.default) for a in self.flags.values() }

        self.handler(*args, **kwargs)

    def parse_with(self, parser, argv, run=False):
        """
        run with supplied args/flags (u-prefixed)

        returns a number indicating the exit code, but raises no errors.
        """

        unnamed_arg = 1
        foo: str = 3
        foo += 1
        for arg in self.arguments:
            if arg.name is None:
                name = f"arg{unnamed_arg}"
                unnamed_arg += 1
            else:
                name = arg.name

            attr = {
                "default": arg.default,
                "type": str if arg.type is ANY else arg.type,
                "nargs": None if (arg.required or arg.default is NO_DEFAULT) else "?",
            }
            parser.add_argument(name, **attr)

        for flag in self.flags.values():
            if flag.kind == FLAG_LONG:
                name = flag.name
                while flag.name.startswith("---"):
                    name = name[1:]
                while not name.startswith("--"):
                    name = f"-{name}"
            elif flag.kind == FLAG_SHORT:
                name = flag.name
                while flag.name.startswith("--"):
                    name = name[1:]
                while not name.startswith("-"):
                    name = f"-{name}"
                # short flags should always be - and one alhpanumeral
                assert len(name) == 2

            attr = {
                "default": flag.default,
            }
            if flag.type is bool:
                attr["action"] = "store_true"
            elif flag.type is int:
                attr["action"] = CountOrValueAction
                attr["nargs"] = "?"
                attr["const"] = 1
                attr["default"] = flag.default if type(flag.default) is int else 0
            else:
                attr["nargs"] = (
                    None if (flag.required or flag.default is NO_DEFAULT) else "?"
                )
                attr["type"] = flag.type
                attr["action"] = ParseOptionalFlag

            parser.add_argument(name, **attr)

        if run == False:
            return

        try:
            return parser.parse_args(argv)
        except SystemExit:
            return 1
