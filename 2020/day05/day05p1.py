#!/usr/bin/env python
import os
import sys
import time
with open(os.path.join(sys.path[0],'day05.data')) as fp:
   lines = [x.strip() for x in fp.readlines()]

starttime=time.time()

maxid = 0
for line in lines:
    maxrow = 127; minrow = 0
    maxcol = 7;   mincol = 0
    for num,ltr in enumerate(line):
        midrow = maxrow-(((maxrow+1)-minrow)/2)
        midcol = maxcol-(((maxcol+1)-mincol)/2)
        if(ltr == "F"): 
            maxrow = midrow
        elif(ltr == "B"):
            minrow = midrow
        elif(ltr == "L"): 
            maxcol = midcol
        elif(ltr == "R"): 
            mincol = midcol
    # print(f"row: {maxrow} ({minrow})\tcol: {maxcol} ({mincol} ID: {(maxrow*8)+maxcol}")
    id = (maxrow*8)+maxcol
    maxid = max(id,maxid)

print(maxid)
print(f"Time: {(time.time()-starttime)*1000:0.4}ms")