#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
from itertools import combinations
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day10.data')

jolt = 0; joltdiff = dict(); difflist = list()
for line in sorted(lines):
    if line-jolt in joltdiff.keys():
        joltdiff[line-jolt] += 1
    else:
        joltdiff[line-jolt] = 1
    difflist.append(line-jolt)
    jolt = line
joltdiff[3] += 1  # Add the last +3 for the device
# print(joltdiff)
print("p1:", joltdiff[3] * joltdiff[1])

## Part2 inspired by
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9ekff/?utm_source=reddit&utm_medium=web2x&context=3


permmultiplier = [1, 1, 2, 4, 7, 13, 24]

perms = 1
prev = 0
onecount = 0
print(difflist)
for jd in difflist:
    if jd == 1:
        onecount += 1
    else:
        print(f"oc={onecount} {permmultiplier[onecount]}")
        perms *= permmultiplier[onecount]
        onecount = 0
    prev = jd
perms *= permmultiplier[onecount]
print(perms)
    
AOC.printTimeTaken()
