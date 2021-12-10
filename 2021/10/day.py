from typing import List
import math
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)


   #  ): 3 points.
   #  ]: 57 points.
   #  }: 1197 points.
   #  >: 25137 points.
def checkline(line: str) -> int:
   lastseen = []
   for token in line:
      if not lastseen:
         lastseen.append(token)
      else:
         if token in "<[({":
            lastseen.append(token)
         elif token in ">)}]":
            last = lastseen.pop()
            if token == ")" and not last == "(":
               # print(f"wrong: {lastseen} {token}")
               return 3
            if token == "]" and not last == "[":
               # print(f"wrong: {lastseen} {token}")
               return 57
            if token == "}" and not last == "{":
               # print(f"wrong: {lastseen} {token}")
               return 1197
            if token == ">" and not last == "<":
               # print(f"wrong: {lastseen} {token}")
               return 25137
   return 0

def checkline2(line: str) -> int:
   lastseen = []
   for token in line:
      if not lastseen:
         lastseen.append(token)
      else:
         if token in "<[({":
            lastseen.append(token)
         elif token in ">)}]":
            last = lastseen.pop()
            if token == ")" and not last == "(":
               return ""
            if token == "]" and not last == "[":
               return ""
            if token == "}" and not last == "{":
               return ""
            if token == ">" and not last == "<":
               return ""
   return lastseen

def autocompletepoints(missing: List) -> int:
   getpoint = {'(':1, "[": 2, "{": 3, "<": 4}
   ret = 0
   while missing:
      t = missing.pop()
      # print(f"{ret} - {getpoint[t]}")
      ret *= 5
      ret += getpoint[t]
   return ret

def part1(linput: List) -> int:
   ret = 0
   for line in linput:
      ret += checkline(line)
   return ret

def part2(linput: List) -> int:
   ret = []
   for line in linput:
       missing = checkline2(line)
       if missing:
          ret.append(autocompletepoints(missing))
   # print(ret)
   return sorted(ret)[math.floor(len(ret)/2)]


assert part1(TEST) == 26397
assert part2(TEST) == 288957
# print("Part 1 TEST (26397)", part1(TEST))
# print("Part 2 TEST (288957)", part2(TEST))
print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
