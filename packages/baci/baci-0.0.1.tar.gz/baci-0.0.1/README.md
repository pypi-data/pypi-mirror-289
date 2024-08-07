# WIP!! This is incomplete/theoretical examples!

# baci - very simple cli framework (for the very lazy)

Got No time to learn and download a huge framework just
to make some simple clis? Yeah me neither I got a board game
meetup to get to after this!

Why not just write a bunch of _vanilla python functions_ and
let baci deal with the weird linux stuff?!

```python
# cli.py

# this can already be a cli command!
def say_hello():
    # docstring adds a description to --help options
    """Prints hello to the screen"""
    print("hello lazy!")

if __name__ == '__main__':
    from baci import Baci
    baci = Baci(commands=(say_hello,))
    baci.run()
```

```
$ python cli.py say-hello
hello lazy!
```

But generally you would add an entrypoint to your cli
that discovers _all_ functions:

```python
from baci import Baci

baci.autorun(dir="./commands")
```

_All non-private defined functions in `commands/` will be registerd in the cli_

Prefix a function with a `_` to be ignored. That's the only way.

## philosophies

### Be a strong, independent package who don't need no pypi

Dependencies means vulnerabilities, which means frequent patching
and updating. WHO GOT TIME FOR DAT?

Write it all in-house.

### Update like it's moving apartments

Would you move to a new studio bedroom every month?

Command line syntax hasn't changed for decades, what's there to update?

Make it feature complete and reliable.

The only exceptions are if there's a bug. Just like in your apartment, you
would make the effort to get rid of bugs.

### There's no zen here, bub!

We don't follow zen of python. Zen is nice but we live in the real
world, ya dig? No bad-ass mf got time for explicitly stating everything.
So just learn the conventions here once and save big on keystrokes!

