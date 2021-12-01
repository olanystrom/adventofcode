from typing import List, Union
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input')

TEST= [199,200,208,210,200,207,240,269,260,263]

def increased(input: List) -> int:
    inc = 0
    last = None
    for i,a in enumerate(input):
        if i == 0:
            last = a
        else:
            if a > last:
                inc += 1
        last = a
    return inc

def increased3(input: List) -> int:
    inc = 0
    for i,a in enumerate(input):
        if i > 2:
            # tmp = input[i-1] + input[i-2]
            last3 = input[i-3]  # + tmp
            current3 = input[i] # + tmp
            if current3 > last3:
                inc += 1
    return inc


assert increased3(TEST) == 5
assert increased(TEST) == 7
print("Part 1", increased(lines))
print("Part 2", increased3(lines))
AOC.printTimeTaken()
