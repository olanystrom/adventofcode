#!/usr/bin/env python
import itertools
import math
import numpy as np
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day12.data')

ourpos = np.array((0,0))
waypoint = np.array((1,10))

def rotate_origin_only(xy, radians):
    """Only rotate a point around the origin (0, 0)."""
    x, y = xy
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)
    return round(xx), round(yy)

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction in 'NEWSF':
        print(f"Going {direction} for >{distance}<")
        if direction == 'F':
            # print("op", ourpos[0],ourpos[1])
            ourpos += waypoint*distance
            # print("wp", waypoint[0],waypoint[1])
            # print("op", ourpos[0],ourpos[1])
        elif direction == "N":
            waypoint += (distance, 0)
            # print("wp", waypoint[0],waypoint[1])
            # print("op", ourpos[0],ourpos[1])
        elif direction == "S":
            waypoint -= (distance, 0)
            # print("wp", waypoint[0],waypoint[1])
            # print("op", ourpos[0],ourpos[1])
        elif direction == "W":
            waypoint -= (0,distance)
            # print("wp", waypoint[0],waypoint[1])
            # print("op", ourpos[0],ourpos[1])
        elif direction == "E":
            waypoint += (0,distance)
            # print("wp", waypoint[0],waypoint[1])
            # print("op", ourpos[0],ourpos[1])
    elif direction in 'LR':
        # print(f"Rotating {distance} to {direction}")
        # print("wp", waypoint[0],waypoint[1])
        # print("op", ourpos[0],ourpos[1])
        if direction == 'R':
            theta = math.radians(-int(distance))
        else:
            theta = math.radians(int(distance))
        waypoint = np.array(rotate_origin_only(waypoint,theta))
        # print("wp", waypoint[0],waypoint[1])
        # print("op", ourpos[0],ourpos[1])
            
print("wp", waypoint[0],waypoint[1])
print("op", ourpos[0],ourpos[1])
print(abs(ourpos[0]) + abs(ourpos[1]))
AOC.printTimeTaken()