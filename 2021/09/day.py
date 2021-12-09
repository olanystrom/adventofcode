from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)

def lowpoint(data: List, x: int, y: int) -> bool:
    testmatrix = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    point = int(data[x][y])
    low = True
    maxy = len(data[0])
    maxx = len(data)
    for test in testmatrix:
        x1, y1 = test
        x2 = x+x1; y2 = y+y1
        if x2 >= maxx or y2 >= maxy or x2 < 0 or y2 < 0:
            continue 
        if int(data[x2][y2]) <= point:
            low = False
    return low

def part1(linput: List) -> int:
   risktot = 0
   for x in range(len(linput)):
      for y in range(len(linput[0])):
         # print(f"{x=},{y=}")
         if lowpoint(linput, x, y):
            risktot += int(linput[x][y]) + 1
               # print(f"{x=} {y=} {linput[x][y]=}")
   return risktot
      

def part2(linput: List) -> int:
   return 0


# assert part1(TEST) == 15
# assert part2(TEST) == x
# print("Part 1 TEST (15)", part1(TEST))
# print("Part 2 TEST (x)", part2(TEST))
print("Part 1", part1(lines))
# print("Part 2", part2(lines))
AOC.printTimeTaken()
