#!/usr/bin/env python
with open('day001.data') as fp:
   lines = [int(x.strip()) for x in fp.readlines()]

def three(lines):
    for line in lines:
        for line2 in lines:
            for line3 in lines:
                if(line + line2 + line3 == 2020):
                    return(line*line2*line3)

print(three(lines))