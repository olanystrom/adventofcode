from typing import List
import sys
from statistics import median
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)

def part1(linput: List) -> int:
   pos = [int(a) for a in linput.split(",")]
   m = median(pos)
   return sum([abs(a-m) for a in pos])

def part2(linput: List) -> int:
   pos = [int(a) for a in linput.split(",")]
   med = median(pos)

   oldsumma, summa = 999999999999, 0
   for m in range(int(med), max(pos)):
      summa = sum([(abs(a-m)*(abs(a-m)+1)/2) for a in pos])
      if summa > oldsumma:
         print(f"{med=} {m=}")
         break
      else:
         oldsumma = summa
   return int(oldsumma)


# assert part1(TEST) == 37
# assert part2(TEST) == 168
# print("Part 1 TEST (37)", part1(TEST[0]))
# print("Part 2 TEST (168)", part2(TEST[0]))
# print("Part 1", part1(lines[0]))
print("Part 2", part2(lines[0]))
AOC.printTimeTaken()
