from argparse import Action


class CountOrValueAction(Action):
    """
    Intended to handle short flags being specified by a number value
    Or repeating the flags (`-v 3` or `-vvv`, respectively)

    Example

        parser = argparse.ArgumentParser()
        parser.add_argument('-v', nargs='?', const=1, default=0,
            action=CountOrValueAction
        )
    """

    def __call__(self, parser, namespace, values, option_string=None):
        if isinstance(values, str) and values.startswith(option_string[-1]):
            count = len(values) + 1
            setattr(namespace, self.dest, count)
        else:
            setattr(namespace, self.dest, int(values))


def _parse_int(i):
    try:
        return int(i)
    except:
        return None

class ParseOptionalFlag(Action):
    """
    Default action for a flag with no annotation. Will parse a decision
    based on a number of things:


    """

    def __init__(self, option_strings, dest, **kwargs):
        if "nargs" in kwargs:
            del kwargs["nargs"]
        super().__init__(option_strings, dest, nargs="*", **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            # flag was given with no value.
            setattr(namespace, self.dest, True)
        elif _parse_int(values[0]):
            setattr(namespace, self.dest, _parse_int(values[0]))
        else:
            setattr(namespace, self.dest, values[0])

