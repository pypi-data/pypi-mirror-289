import argparse

from baci.actions import ParseOptionalFlag


class BaciHelpFormatter(argparse.HelpFormatter):
    """
    The custom formatter for baci applications
    """

    def _format_action_invocation(self, action):
        if isinstance(action, ParseOptionalFlag):
            return f"{action.option_strings[0]}"
        else:
            return super()._format_action_invocation(action)

    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = "usage: \n  "
        usage_parts = [prefix]
        if usage is not None:
            usage_parts.append(usage)
        else:
            prog = self._prog
            optionals = []
            positionals = []
            for action in actions:
                if action.option_strings:
                    if action.dest == "help":
                        continue
                    if isinstance(action, ParseOptionalFlag):
                        optionals.append(f"[{action.option_strings[0]}]")
                    else:
                        optionals.append(self._format_action_invocation(action))
                else:
                    positionals.append(self._format_action_invocation(action))
            usage_parts.append(prog)
            usage_parts.extend(optionals)
            usage_parts.extend(positionals)
        message = ' '.join(usage_parts)
        return f"{message}\n"
