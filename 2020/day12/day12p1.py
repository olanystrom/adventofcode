#!/usr/bin/env python
import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day12.data')


RotateRight = 'ESWN'
current = 0
posx = 0
posy = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction in 'NEWSFB':
        print(f"Going {direction} for >{distance}<")
        if direction == 'F':
            direction = RotateRight[current]
        if direction == "N":
            posx -= distance
            # print(posx,posy)
        elif direction == "S":
            posx += distance
            # print(posx,posy)
        elif direction == "W":
            posy -= distance
            # print(posx,posy)
        elif direction == "E":
            posy += distance
            # print(posx,posy)
    elif direction in 'LR':
        if direction == 'R':
            # print(f"Rotating {int(distance)/90} steps to {direction} from {RotateRigth[current]} to {RotateRigth[(int(current+int(distance)/90))%4]}")
            current = (int(current+(distance/90))%4)
        else:
            print(f"Rotating {int(distance)/90} steps to {direction} from {RotateRight[current]} to {RotateRight[(int(current-int(distance)/90)%4)]}")
            current = (int(current-(distance/90))%4)
            
print(posx,posy)
print(abs(posx) + abs(posy))
AOC.printTimeTaken()