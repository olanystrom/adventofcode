#!/usr/bin/env python
with open('day001.data') as fp:
   lines = fp.readlines()

lines = [int(x.strip()) for x in lines] 

for line in lines:
    for line2 in lines:
        for line3 in lines:
            if(line + line2 + line3 == 2020):
                print(f"answer: {line*line2*line3}\n")
                exit()