#!/usr/bin/env python
import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day13.data')

num = int(lines[0])
#times = lines[1]split(',')
times=[int(x) for x in lines[1].split(',') if x.isdigit()]

dist = 0
mindist = num
for x in times:
    dist = (x - num%x)
    if dist < mindist:
        mindist = dist
        buss = x
print(f"dist: {mindist} med {buss} svar: {mindist*buss}")
