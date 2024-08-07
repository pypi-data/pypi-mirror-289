import inspect
import itertools

from typing import List
from baci.models._command import (
    Command,
    Argument,
    ARGUMENT,
    FLAG_SHORT,
    FLAG_LONG,
    NO_DEFAULT,
)
from baci.util import get_alias_annotation, get_cast_annotation, to_snake_case


def _argument_from_param(param: inspect.Parameter) -> List[Argument]:
    """
    Creates a list of Arguments from a function parameter

    In the case of a flag argument with an alias (def a(*, foo: 'f')),
    a list with both FLAG_SHORT and FLAG_LONG versions are returned,
    otherwise a list of 1 Argument is returned.
    """
    arguments = []

    # attribute parsing
    type = get_cast_annotation(param.annotation)
    default = NO_DEFAULT if param.default is inspect._empty else param.default
    if param.kind in (
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
    ):
        kind = ARGUMENT
        required = True if default is NO_DEFAULT else False
    elif param.kind is inspect.Parameter.KEYWORD_ONLY:
        # `def h(*, foo)` kwonly are interpreted as flags
        # single letter is short flag (`f`) = -f
        # full word is long flag (`force`) = --force
        # annotate with string to give long and short version (`force: 'f'`)

        required = True if param.annotation == 1 else False
        # TODO required can be True if annotated with 1 or the Flag(required=True) class,
        # we're not doing that yet
        kind = FLAG_SHORT if len(param.name) == 1 else FLAG_LONG

        # create alias

    if (kind in (FLAG_SHORT, FLAG_LONG)) and (
        alias := get_alias_annotation(param.annotation)
    ):
        arguments.append(
            Argument(
                "",
                name=to_snake_case(alias),
                type=type,
                kind=FLAG_SHORT if len(alias) == 1 else FLAG_LONG,
                default=default,
                required=required,
            )
        )

    arguments.append(
        Argument(
            "",
            name=to_snake_case(param.name),
            type=type,
            kind=kind,
            default=default,
            required=required,
        )
    )
    return arguments


def from_function(function) -> Command:
    name = to_snake_case(function.__name__)
    params = inspect.signature(function).parameters

    arguments = list(
        itertools.chain(*[_argument_from_param(p) for p in params.values()])
    )

    return Command(name, function, arguments=arguments)
