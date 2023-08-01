# https://adventofcode.com/2020/day/6

import sys

allS = []
S = set()
allT = []
T = set()

start = True

for line in sys.stdin:
    if line == '\n':
        allS.append(S.copy())
        S.clear()
        allT.append(T.copy())
        T.clear()
        start = True
    else:
        S |= { x for x in line.strip() }
        if not start:
            T &= set(list(line.strip()))
        else:
            T = set(line.strip())
            start = False

allS.append(S)
allT.append(T)

print("Part 1")
print(sum(map(len, allS)))
print("Part 2")
print(sum(map(len, allT)))
