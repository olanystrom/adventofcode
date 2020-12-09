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

def xmas_hack2(num,buffer):
    for i in range(len(buffer) - 1):
        _sum = buffer[i]
        _list = [buffer[i]]
        j = i + 1
        while _sum + buffer[j] <= num:
            _sum += buffer[j]
            _list.append(buffer[j])
            j += 1
        if _sum == num:
            print(min(_list) + max(_list))

for num,line in enumerate(lines):
    if num < preamble:
        next
    else:
        if not xmas_check(line,lines[num-preamble:num]):
            print(f"xmas failed at line {num} with {line}")
            xmas_hack2(line,lines[0:num])
AOC.printTimeTaken()