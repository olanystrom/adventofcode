from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)

class Line():
   def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
       self.x1 = x1
       self.x2 = x2
       self.y1 = y1
       self.y2 = y2

def print_matrix(lines: dict) -> None:
   for y in range(0, 11):
      for x in range(0, 11):
         dot = lines.get((x,y), 0)
         if dot == 0:
            print(".", end="")
         else:
            print(dot, end="")
      print()

def part1(linput: List) -> int:
   my_lines = dict()
   for line in linput:
      xy1, xy2 = line.split(" -> ")
      x1,y1 = xy1.split(",")
      x2,y2 = xy2.split(",")
      line = Line(x1=int(x1), x2=int(x2), y1=int(y1), y2=int(y2))
      if line.x1 == line.x2:
         x = line.x1
         if line.y2 > line.y1:
            for y in range(line.y1, line.y2+1):
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
         else:
            for y in range(line.y1, line.y2-1, -1):
               # print(f"{x=}, {y=}")
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
      elif line.y1 == line.y2:
         y = line.y1
         if line.x2 > line.x1:
            for x in range(line.x1, line.x2+1):
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
         else:
            for x in range(line.x1, line.x2-1, -1):
               # print(f"{x=}, {y=}")
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
   # print_matrix(my_lines)
   return len([a for a in my_lines.values() if a > 1])


def part2(linput: List) -> int:
   my_lines = dict()
   for line in linput:
      xy1, xy2 = line.split(" -> ")
      x1,y1 = xy1.split(",")
      x2,y2 = xy2.split(",")
      line = Line(x1=int(x1), x2=int(x2), y1=int(y1), y2=int(y2))
      if line.x1 == line.x2:
         x = line.x1
         if line.y2 > line.y1:
            for y in range(line.y1, line.y2+1):
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
         else:
            for y in range(line.y1, line.y2-1, -1):
               # print(f"{x=}, {y=}")
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
      elif line.y1 == line.y2:
         y = line.y1
         if line.x2 > line.x1:
            for x in range(line.x1, line.x2+1):
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
         else:
            for x in range(line.x1, line.x2-1, -1):
               # print(f"{x=}, {y=}")
               my_lines[x, y] = my_lines.get((x, y), 0) + 1
      elif abs(line.x1 - line.x2) == abs(line.y1 - line.y2):
         x1,x2 = line.x1, line.x2
         y1,y2 = line.y1, line.y2
         x,y = x1,y1
         if x1 > x2:
            xdelta = -1
         else:
            xdelta = 1
         if y1 > y2:
            ydelta = -1
         else:
            ydelta = 1
         # print(f"Diagonal: {x1},{y1} {x2},{y2}")
         for diag in range(abs(line.x1 - line.x2)+1):
               xdiag = diag * xdelta
               ydiag = diag * ydelta
               val = my_lines.get((x+xdiag, y+ydiag), 0) + 1
               # print(f"D {x+xdiag},{y+ydiag} : {val}")
               my_lines[x+xdiag, y+ydiag] = val
   # print_matrix(my_lines)
   return len([a for a in my_lines.values() if a > 1])


assert part1(TEST) == 5
assert part2(TEST) == 12
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
# print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
