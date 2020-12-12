#!/usr/bin/env python
from functools import lru_cache
import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day11.data')


class Seating():
    def __init__(self,world):
        self.world = world
        self.occ = 0
        self.maxx = len(self.world)-1
        self.maxy = len(self.world[0])-1
        self.checkmatrix = list(filter(self.not00, itertools.product((1,0,-1),repeat=2)))

    def not00(self, x):
        return x != (0,0)

    def occaround(self, x, y):
        count = 0; 
        for (i,j) in self.checkmatrix:
            if 0 <= x+i <= self.maxx:
                if 0 <= y+j <= self.maxy:
                    if self.world[x+i][y+j] == "#":
                        count += 1
        return count

    def count_occ(self):
        self.occ = 0
        for line in self.world:
            self.occ += line.count('#')

    def oneround(self):
        """
        * If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        * If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        * Otherwise, the seat's state does not change.
        """
        work = self.world.copy()
        for i, line in enumerate(self.world):
            for j, space in enumerate(line):
                if space in "L#":
                    around = self.occaround(i,j); # print(around)
                    if space == "L" and around == 0:
                        work[i] = work[i][:j] + "#" + work[i][j + 1:]
                    elif space == "#" and around >= 4:
                        work[i] =  work[i][:j] + "L" + work[i][j + 1:]
        if self.world == work:
            self.count_occ()
            return False
        self.world = work
        return True


seating = Seating(lines)
rounds = 0
while True:
    if seating.oneround():
        rounds += 1
    else:
        break
print(rounds)
print(seating.occ)
AOC.printTimeTaken()