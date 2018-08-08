import sys
import os.path
from soccer import Score

if sys.argv.__len__() > 1:
    filename = sys.argv[1]
    if os.path.isfile(filename):
        lines = [line.rstrip('\n') for line in open(filename)]
        print(Score.rank(lines))
