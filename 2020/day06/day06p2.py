#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day06.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

total = 0; groupsize = 0; answers = dict()
for line in lines:
   if line == "":
      total += len([c for c in answers if answers[c] == groupsize])
      answers = dict();  groupsize = 0
   else:
      groupsize += 1
      for a in set(line):
         if a in answers.keys():
            answers[a] += 1
         else:
            answers[a] = 1

print(total)   