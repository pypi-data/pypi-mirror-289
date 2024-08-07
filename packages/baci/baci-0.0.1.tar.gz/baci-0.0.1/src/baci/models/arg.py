"""
The Arg annotation for baci functions
"""

from baci.models._command import NO_DEFAULT


class Arg:
    """
    The Arg annotation to add metadata to a cli command.

    :param type:
    """

    def __init__(
        self, description, *, type=None, check=None, default=NO_DEFAULT, required=None
    ):
        self.description = description
        self.type = type or []
        self.check = check
        self.default = default
        self.required = required
