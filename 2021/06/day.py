from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)


def nextday(fish: List[int]) -> List[int]:
   newfish = []
   for a in fish:
      if a > 0:
         newfish.append(a-1)
      else:
         newfish.append(6)
         newfish.append(8)
   return newfish

def nextfday(fish) -> dict:
   newfish = dict()
   for a in range(1,10):
      newfish[a-1] = fish.get(a, 0)
   newfish[6] += fish[0]
   newfish[8] = fish[0]
   return newfish


def fishdays(fish: List[int]) -> dict:
   fishd = dict()
   for i in range(10):
      fishd[i] = sum([1 for a in fish if a == i])
   return fishd

def part1(linput: List, days: int=18) -> int:
   fish = [int(a) for a in linput.split(',')]
   for a in range(days):
      fish = nextday(fish)
   return len(fish)

def part2(linput: List, days=256) -> int:
   fish = [int(a) for a in linput.split(',')]
   fishd = fishdays(fish)
   for a in range(days):
      fishd = nextfday(fishd)
   return sum(fishd.values())


assert part1(TEST[0]) == 26
assert part1(TEST[0], days=80) == 5934
# assert part2(TEST) == 230
print("Part 1 TEST", part1(TEST[0]))
print("Part 1 (80) TEST", part1(TEST[0], 80))
# print("Part 2 TEST", part2(TEST))
# print("Part 2 (256) TEST", part2(TEST[0], 256))
print("Part 1", part1(lines[0], 80))
print("Part 2", part2(lines[0], 256))
AOC.printTimeTaken()
