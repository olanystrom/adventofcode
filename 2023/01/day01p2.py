import AOC
lines: list = AOC.loadInput(None, 'input.txt', notInt=True)
TEST: list = AOC.loadInput(None, 'test2.txt', notInt=True)

num1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num2 = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

num = list()
for a in lines:
    for replacement in zip(num1, num2):
        a = a.replace(*replacement)
    print(f"{a=}")
    first = "X"
    last = "X"
    for f in a:
        if f in "0123456789":
            first = f
            break
    for f in a[::-1]:
        if f in "0123456789":
            last = f
            break
    num.append(int(f"{first}{last}"))
    print(int(f"{first}{last}"))
print(sum(num))