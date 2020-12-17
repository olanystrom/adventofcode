#!/usr/bin/env python
from functools import lru_cache
import itertools
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day17.data')

""" Day 17: Conway Cubes """

# lines = [".#.", "..#", "###"] ## TEST t1 (x, y )

"""
During a cycle, all cubes simultaneously change their state according to the following rules:
* If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
* If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
"""

class CCubes():
    def __init__(self,world, dim):
        self.world = set()
        self._build2d(world, dim)
        self.dim = dim
        self.n = len(world[0])+1
        self.checkmatrix = list(itertools.product((1,0,-1),repeat=dim))
        self.checkmatrix.remove((0,) * dim)  # Dont check self/origin
        # print(f"{len(self.checkmatrix)=}")

    def set(self, xyz):
        self.world.add(xyz)

    def delete(self, xyz):
        if xyz in self.world:
            self.world.remove(xyz)

    def _build2d(self, world, dim):
        for x,xl in enumerate(world):
            for y,yl in enumerate(xl):
                if yl == '#':
                    xyz = tuple(list((x,y)) + [0] * (dim-2))
                    self.set(xyz)

    def checknodes(self, world):
        cmatrix = set(itertools.product((1,0,-1),repeat=self.dim))
        for (x,y,z) in world:
            for (i,j,k) in cmatrix:
                yield (x+i, y+j, z+k)

    def around3d(self, myxyz, world):
        count = 0;
        (x,y,z) = myxyz
        for (i,j,k) in self.checkmatrix:
            if (x+i, y+j, z+k) in world:
                count +=1
        return count

    def oneround(self):
        """
        * If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        * If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        """
        oldworld = self.world.copy()
        # print(oldworld)
        for a in set(self.checknodes(oldworld)):
            around = self.around3d(a, oldworld)
            if a in oldworld:
                if str(around) not in "23":
                    self.delete(a)
            else:
                if around == 3:
                    self.set(a)
        self.n += 1
        return True

cubeworld = CCubes(lines, 3)

cubeworld.oneround()
cubeworld.oneround()
cubeworld.oneround()
cubeworld.oneround()
cubeworld.oneround()
cubeworld.oneround()
print(len(cubeworld.world))

AOC.printTimeTaken()