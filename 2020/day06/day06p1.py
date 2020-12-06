#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day06.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

total = 0; answers = ""
for line in lines:
   if line == "":
      total += len(set(answers))
      answers = ""
   else:
      answers += line 

print(total)   