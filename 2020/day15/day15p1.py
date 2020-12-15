#!/usr/bin/env python
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day15.data')

""" Day 15: Rambunctious Recitation """

testdata = list((0,0,3,6)) ## => 438
data = list((0,0,12,6,13,20,1,17))
# data = list((0,0,3,6)) 

start = len(data)-1
stop = 2020

"""
If that was the first time the number has been spoken, the current player says 0.
Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
"""

for a in range(start,stop):
    # print('-'*20)
    # print(data)
    num = data[-1]
    if (num in data[:-1]):
        index2 = data[:-1][::-1].index(num)+1
        # index = [index for index,value in enumerate(data[:-1]) if value == num][-1]
        # print(f"a: {a} i: {index}, a-i: {a-index}, i2: {index2}")
        data.append(index2)
        # print(data[-1])
    else:
        data.append(0)
print(data)
print(data[-1])
AOC.printTimeTaken()