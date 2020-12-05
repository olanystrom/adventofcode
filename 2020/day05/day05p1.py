#!/usr/bin/env python
import os
import sys
with open(os.path.join(sys.path[0],'day05.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]


maxid = 0
for line in lines:
    maxrow = 127
    minrow = 0
    maxcol = 7
    mincol = 0
    for num,ltr in enumerate(line):
        if num < 7:
            if(ltr == "F"): # 32 - 63 => 32 - 47 
                maxrow = maxrow-(((maxrow+1)-minrow)/2)
            elif(ltr == "B"):  #  32-47 => 40-47
                minrow = minrow + (((maxrow+1)-minrow)/2)
        else:
            if(ltr == "L"): # 32 - 63 => 32 - 47 
                maxcol = maxcol-(((maxcol+1)-mincol)/2)
            elif(ltr == "R"):  #  32-47 => 40-47
                mincol = mincol + (((maxcol+1)-mincol)/2)
    # print(f"row: {maxrow} ({minrow})\tcol: {maxcol} ({mincol} ID: {(maxrow*8)+maxcol}")
    id = (maxrow*8)+maxcol
    
    if id > maxid:
        maxid = id

print(maxid)