# https://adventofcode.com/2021/day/12

import sys
from collections import namedtuple

cave = namedtuple('cave', ['id', 'small', 'N'])

C = {}

def count_path(c, S):
    if c.id == "end":
        return 1
    if c.small and c.id in S:
        return 0
    result = 0
    for n in c.N:
        T = S
        if c.small:
            T = T | { c.id }
        result += count_path(C[n], T)
    return result

def count_path_part2(c, D):
    if c.id == "end":
        return 1
    if c.id == "start" and D["start"] == 1:
        return 0
    if c.small and D[c.id] == 2:
        return 0
    if c.small and D[c.id] == 1 and any(x == 2 for x in D.values()):
        return 0
    result = 0
    for n in c.N:
        E = D
        if c.small:
            E = E.copy()
            E[c.id] += 1
        result += count_path_part2(C[n], E)
    return result


for line in sys.stdin:
    c1,c2 = line.strip().split('-')
    if c1 not in C.keys():
        C[c1] = cave(c1, c1.islower(), [c2])
    else:
        C[c1].N.append(c2)
    if not c2 in C.keys():
        C[c2] = cave(c2, c2.islower(), [c1])
    else:
        C[c2].N.append(c1)

SS = set()
print("Part 1")
print(count_path(C["start"], SS))

DD = { c.id: 0 for c in C.values() if c.small }
print("Part 2")
print(count_path_part2(C["start"], DD))