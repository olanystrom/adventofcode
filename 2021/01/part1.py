from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'input')

TEST= [199,200,208,210,200,207,240,269,260,263]

def increased(input: List) -> int:
    inc = 0
    for i,a in enumerate(input):
        if i == 0:
            last = a
        else:
            if a > last:
                inc += 1
        last = a
    return inc

assert increased(TEST) == 7
print("Part 1", increased(lines))
