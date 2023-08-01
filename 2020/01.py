# https://adventofcode.com/2020/day/1

import sys

S = set()
T = []

for line in sys.stdin:
    x = int(line)
    if 2020 - x in S:
        print("Part 1")
        print(x * (2020-x))
    S.add(x)
    T.append(x)

for a in range(len(T)):
    for b in range(a+1,len(T)):
        for c in range(b+1,len(T)):
            if T[a] + T[b] + T[c] == 2020:
                print("Part 2")
                print(T[a] * T[b] * T[c])
