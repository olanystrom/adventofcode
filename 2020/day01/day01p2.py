#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0], 'day01.data')) as fp:
   lines = [int(x.strip()) for x in fp.readlines()]

for line in lines:
    for line2 in lines:
        for line3 in lines:
            if(line + line2 + line3 == 2020):
                print(f"answer: {line*line2*line3}\n")
                exit()