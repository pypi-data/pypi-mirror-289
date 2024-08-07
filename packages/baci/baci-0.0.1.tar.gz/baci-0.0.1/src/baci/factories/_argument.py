from baci.models._command import Argument, ARGUMENT, FLAG_SHORT, FLAG_LONG, NO_DEFAULT


def from_arg(arg, name):
    """
    Combines the param name with the annotation to get
    complete Argument data
    """
    if arg.required is None:
        required = True if arg.default is NO_DEFAULT else False
    else:
        required = True

    return Argument(
        description=arg.description,
        name=name,
        type=arg.type,
        check=arg.check,
        default=arg.default,
        required=required,
        kind=ARGUMENT,
    )


def from_flag(flag, name) -> list:
    argument = Argument(
        name=name,
        description=flag.description,
        type=flag.type,
        check=flag.check,
        default=flag.default,
        required=flag.required,
        kind=FLAG_SHORT if len(name) == 1 else FLAG_LONG,
    )
    if flag.alias:
        return [
            argument,
            Argument(
                description=flag.description,
                type=flag.type,
                check=flag.check,
                default=flag.default,
                required=flag.required,
                name=flag.alias,
                kind=FLAG_SHORT if len(flag.alias) == 1 else FLAG_LONG,
            ),
        ]
    return [argument]
