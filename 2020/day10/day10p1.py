#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
from itertools import combinations
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(10)

jolt = 0; joltdiff = dict()
for line in sorted(lines):
    if line-jolt in joltdiff.keys():
        joltdiff[line-jolt] += 1
    else:
        joltdiff[line-jolt] = 1
    jolt = line
joltdiff[3] += 1  # Add the last +3 for the device
# print(joltdiff)
print(joltdiff[3] * joltdiff[1])
AOC.printTimeTaken()