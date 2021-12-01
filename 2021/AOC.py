from time import time
import os
import sys

_startTime = None

def loadInput(day = None, filename = False):
    global _startTime

    if day:
        day = str(day)
    if not filename:
        filename = "day" + day.zfill(2) + ".data"
    filepath = (os.path.join(sys.path[0],filename))

    with open(filepath) as f:
        content = [l.rstrip("\n") for l in f.readlines()]

    _startTime = time()

    if len(content) == 1:
        try:
            return int(content[0])
        except:
            try:
                return [int(i) for i in content[0].split()]
            except:
                return content[0]
    else:
        try:
            return [int(i) for i in content]
        except:
            return content

def printTimeTaken():
    global _startTime
    _endTime = time()
    
    print("Time: {:.3f}s".format(_endTime - _startTime))