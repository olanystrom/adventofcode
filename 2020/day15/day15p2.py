#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day15.data')

""" Day 15: Rambunctious Recitation """


testdata = list((0,0,3,6)) ## => 438
data = list((0,0,12,6,13,20,1))
last = 17
start = len(data)
# stop = 30000
stop = 30000000
# stop = 2020
# data += [-1] * (stop-start)

indexes = dict()

for n,v in enumerate(data):
    indexes[v] = n

"""
If that was the first time the number has been spoken, the current player says 0.
Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
"""
for a in range(start,stop):
    # print("a,l,i", a, last, indexes[last])
    if last in indexes.keys():
        age = a - indexes[last]
    else:
        age = 0
    indexes[last] = a
    last = age

print(last)
AOC.printTimeTaken()