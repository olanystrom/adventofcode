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

def xmas_hack(num,buffer):
    for start in range(len(buffer)):
        offset = 2
        while sum(buffer[start:start+offset]) < num:
            offset += 1
        if sum(buffer[start:start+offset]) == num:
            # print(buffer[start:start+offset])
            # print(f"fount at {start} - {start+offset}")
            _min = min(buffer[start:start+offset])
            _max = max(buffer[start:start+offset])
            print(f"{_min} + {_max} = {_min+_max}")
            return

for num,line in enumerate(lines):
    if num < preamble:
        next
    else:
        if not xmas_check(line,lines[num-preamble:num]):
            print(f"xmas failed at line {num} with {line}")
            xmas_hack(line,lines[0:num])
AOC.printTimeTaken()