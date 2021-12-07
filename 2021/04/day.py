from typing import List
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines: List = AOC.loadInput(None,'input', notInt=True)
TEST: List = AOC.loadInput(None,'test', notInt=True)


class Bingo:
   def __init__(self, id: int, lines: List) -> None:
      self.lines: list = [lines[0]]
      self.id = id
      self.numbers: list = []
      for line in lines[1:]:
         self.lines.append(line)
      self.bingo: bool = False
   
   def __repr__(self) -> str:
      return str(self.id)
      # ret = ""
      # for line in self.lines:
      #    ret += f"{line}\n"
      # return ret

   def printme(self):
      for line in self.lines:
         for num in line:
            if num in self.numbers:
               print(f"\033[1m{num:02d}\033[0m", end=" ")
            else:
               print(f"{num:02d}", end=" ")
         print("")


   def addnumber(self, number: int) -> bool:
      for line in self.lines:
         if number in line:
            # print(f"Found {number} in {self.id=}")
            self.numbers.append(number)
      return self.isbingo()


   def isbingo(self) -> bool:
      for line in self.lines:
         if len([a for a in line if a in self.numbers]) == 5:
            print(f"Bingo line {self.id=}")
            print(f"{line=}")
            print(f"{self.numbers=}")
            return True
      for i in range(5):
         row = set()
         row.update([self.lines[a][i] for a in range(5)])
         if len([a for a in row if a in self.numbers]) == 5:
            print(f"Bingo row {self.id=}")
            print(f"{row=}")
            print(f"{self.numbers=}")
            return True
      return False
   
   def part1score(self) -> int:
      tot = 0
      print(f"{self.numbers=}")
      for line in self.lines:
         line = list(set(line) - set(self.numbers))
         tot += sum(line)
      lastnum = int(self.numbers.pop())
      print(f"Answer = {tot*lastnum}\t{tot=} {lastnum=}")
      return tot*lastnum

def part1(linput: List) -> int:
   board = []
   bcount = 0
   lineiter = iter(linput)
   for line in lineiter:
      if not 'numbers' in locals():
         numbers = [int(a) for a in line.split(",")]
         next(lineiter)
      else:
         if not line:
            bcount += 1
            if not 'bingos' in locals():
               bingos = [Bingo(id = bcount, lines = board)]
            else:
               bingos.append(Bingo(id = bcount, lines = board))
            board = []
         else:
            board.append([int(a) for a in line.split()])
   bingos.append(Bingo(id = bcount+1, lines=board))

   breakme = False
   for i in numbers:
      if breakme:
         break
      for b in bingos:
         if b.addnumber(i):
            bingowinner = b
            print(f"bingo in {b}")
            b.printme()
            breakme = True
   return bingowinner.part1score()


def part2(linput: List) -> int:
   board = []
   lineiter = iter(linput)
   bcount = 0
   for line in lineiter:
      if not 'numbers' in locals():
         numbers = [int(a) for a in line.split(",")]
         next(lineiter)
      else:
         if not line:
            bcount += 1
            if not 'bingos' in locals():
               bingos = [Bingo(id = bcount, lines = board)]
            else:
               bingos.append(Bingo(id=bcount, lines=board))
            board = []
         else:
            board.append([int(a) for a in line.split()])
   bingos.append(Bingo(id = bcount+1, lines = board))

   breakme = False
   removeme = []
   for i in numbers:
      if breakme:
         break
      for xdel in removeme:
         bingos.remove(xdel)
      removeme = []
      for b in bingos:
         if b.addnumber(i):
            bingowinner = b
            # print(f"bingo in {b} ({len(bingos)=}")
            print(f"bingo {len(bingos)=}\n\n")
            if len(bingos) == 1:
               breakme = True
               b.printme()
               bingowinner = b
            else:
               removeme.append(b)
   return bingowinner.part1score()



assert part1(TEST) == 4512
assert part2(TEST) == 1924
# print("Part 1 TEST", part1(TEST))
# print("Part 2 TEST", part2(TEST))
print("Part 1", part1(lines))
print("Part 2", part2(lines))
AOC.printTimeTaken()
