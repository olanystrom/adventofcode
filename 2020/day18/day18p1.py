#!/usr/bin/env python
import itertools
import re
import sys
sys.path.insert(1, sys.path[0] + '/..')  # Add parent of my directory to path
import AOC  ## pylint: disable=import-error
lines = AOC.loadInput(None,'day18.data')

""" Day 18: Operation Order """

"""
However, the rules of operator precedence have changed.
Rather than evaluating multiplication before addition, the operators have the same precedence,
and are evaluated left-to-right regardless of the order in which they appear.
"""

class AoCMath():
    def __init__(self, mymath):
        mymath = mymath.replace(" ", "")
        # print(f"\n{mymath=}")
        while len(list(self.parenthetic_contents(mymath))) > 0:
            level, mmath = list(self.parenthetic_contents(mymath))[0]
            replace1 = f"({mmath})"
            # print(f"{level=} {mmath=}")
            # print(f"{replace1=} {self.evalmath(mmath)=}")
            mymath = mymath.replace(replace1,str(self.evalmath(mmath)))
            # print(f"{mymath=}")
        self.summa = self.evalmath(mymath)


    def evalmath(self, mathline):
        """ Evalutes every operation in order, no paranteces """
        parts = re.split('(\W+)',mathline)
        summa = parts[0]
        for part in parts[1:]:
            if part.isdigit():
                summa = eval(f"{summa}{last}{part}")  
            else:
                last = part
        return summa


    """ https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level """
    def parenthetic_contents(self,string):
        """Generate parenthesized contents in string as pairs (level, contents)."""
        stack = []
        for i, c in enumerate(string):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                start = stack.pop()
                yield (len(stack), string[start + 1: i])


def aocmath(line):
    aocm = AoCMath(line)
    return aocm.summa

# print(aocmath(lines[0]))
totsum = 0
for line in lines:
    # print(aocmath(line))
    totsum += aocmath(line)

print(totsum)
AOC.printTimeTaken()