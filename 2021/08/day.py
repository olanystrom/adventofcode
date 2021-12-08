from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)

def part1(linput: List) -> int:
   tot = 0
   for line in linput:
      _, data = line.split(" | ")
      digits = data.split(" ")
      tot += sum([1 for a in digits if len(a) in [2,3,4,7]])
   return tot

def get0(digits: List[str], answer: dict) -> str:
   # *   0: len(6) all from 7 but not 4
   for dig in digits:
      if len(dig) == 6:
         # print(f"len 6: {dig} (7: {answer[7]})")
         if len(set(dig) - set(answer[7])) == 3:
            # print(f"all of 7: {dig} {answer[7]}")
            if len(set(dig) - set(answer[4])) == 3:
               # print(f"0: {dig}")
               return dig

def get3(digits: List[str], answer: dict) -> str:
   # *   3: len(5) all from 7
   for dig in digits:
      if dig in answer.values():
         continue
      else:
         if len(dig) == 5:
            if len(set(dig) - set(answer[7])) == 2:
               # print(f"3: {dig}")
               return dig

def get9(digits: List[str], answer: dict) -> str:
   # *   9: len(6) all from 4
   for dig in digits:
      if dig in answer.values():
         continue
      else:
         if len(dig) == 6:
            if len(set(dig) - set(answer[4])) == 2:
               return dig

def get6(digits: List[str], answer: dict) -> str:
   # *   6: len(6) one from 1
   for dig in digits:
      if dig in answer.values():
         continue
      else:
         if len(dig) == 6:
            if len(set(dig) - set(answer[1])) == 5:
               return dig

def get5(digits: List[str], answer: dict) -> str:
   # *   5: len(5) 5 from 6
   for dig in digits:
      if dig in answer.values():
         continue
      else:
         if len(dig) == 5:
            if len(set(dig) - set(answer[6])) == 0:
               return dig

def get2(digits: List[str], answer: dict) -> str:
   for dig in digits:
      if dig in answer.values():
         continue
      else:
         if len(dig) == 5:
            return dig

# *   1: len(2)
# *   4: len(4)
# *   7: len(3)
# *   8: len(7)
# *   0: len(6) all from 7 but not 4
# *   3: len(5) all from 7
# *   9: len(6) all from 4
# *   6: len(6) one from 1
# *   5: len(5) 5 from 6
#    2: len(5) 

def part2(linput: List) -> int:
   tot = 0
   for line in linput:
      answer = dict()
      tdata, data = line.split(" | ")
      training = tdata.split(" ")
      digits = data.split(" ")
      # fetch the easy answers
      for digit in training:
         if len(digit) == 2:
            answer[1] = digit
         elif len(digit) == 4:
            answer[4] = digit
         elif len(digit) == 3:
            answer[7] = digit
         elif len(digit) == 7:
            answer[8] = digit
      answer[0] = get0(training, answer)
      answer[3] = get3(training, answer)
      answer[9] = get9(training, answer)
      answer[6] = get6(training, answer)
      answer[5] = get5(training, answer)
      answer[2] = get2(training, answer)

      # numbers = {answer[key]:key for key in answer}

      value = ""
      for dig in digits:
         for a in answer:
            if len(set(dig) - set(answer[a])) == 0:
              if len(set(answer[a]) - set(dig)) == 0:
                  value += str(a)
      # print(f"{tot=} {value=}")
      tot += int(value)
   return tot

assert part1(TEST) == 26
assert part2(TEST) == 61229
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
# print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
