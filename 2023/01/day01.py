import AOC  ## pylint: disable=import-error
lines: list = AOC.loadInput(None,'input.txt', notInt=True)
TEST: list = AOC.loadInput(None, 'test.txt', notInt=True)

num = list()
for a in lines:
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
    # print(f"{first=} {last=}")
print(sum(num))