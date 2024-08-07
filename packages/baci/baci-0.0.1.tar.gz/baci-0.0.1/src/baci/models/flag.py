"""
The Arg annotation for baci functions
"""


class Flag:
    """
    The Flag annotation to add metadata to a cli command.
    """

    def __init__(
        self,
        description,
        *,
        alias: str = None,
        type=None,
        check=None,
        default=None,
        required=False,
    ):
        self.description = description
        self.type = type or []
        self.check = check
        self.default = default
        self.required = required
        self.alias = alias
