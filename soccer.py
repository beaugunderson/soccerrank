import sys
import os.path
from soccer import Score

# always best to use `len` instead of calling `__len__` directly
# and if checking for > 0; can just use equality test (e.g. instead of
# `if len(thing) > 0` you can use `if thing`; it is often faster!
if len(sys.argv) > 1:
    filename = sys.argv[1]

    if os.path.isfile(filename):
        # note that it can often be faster to inline a list comprehension for a
        # generator expression, e.g. instead of first defining a list (which
        # takes memory) you could use:
        # Score.rank(line.rstrip('\n') for line in open(filename))
        # note the lack of []; this will be a generator and not read the entire
        # file at the same time... this can be a real speedup as it allows
        # methods like any() and all() to short-circuit so you never end up
        # building the whole list!
        lines = [line.rstrip('\n') for line in open(filename)]
        print(Score.rank(lines))
