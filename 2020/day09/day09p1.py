#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC
lines = AOC.loadInput(9)

preamble = 25

def xmas_check(num, buffer):
    for a in buffer:
        for b in buffer:
            if (a != b) and (a+b == num):
                return True
    return False

for num,line in enumerate(lines):
    if num < preamble:
        next
    else:
        if not xmas_check(line,lines[num-preamble:num]):
            print(f"xmas failed at line {num} with {line}")
AOC.printTimeTaken()