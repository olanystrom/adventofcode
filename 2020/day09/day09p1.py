#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
from itertools import combinations
import AOC
lines = AOC.loadInput(9)

preamble = 25

def xmas_check(num, buffer):
    for a, b in combinations(buffer, 2):
        if a+b == num:
            return True
    return False

for num,line in enumerate(lines):
    if num < preamble:
        next
    else:
        if not xmas_check(line,lines[num-preamble:num]):
            print(f"xmas failed at line {num} with {line}")
AOC.printTimeTaken()