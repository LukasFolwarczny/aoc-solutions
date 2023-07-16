# https://adventofcode.com/2022/day/18

import sys

sys.setrecursionlimit(10_000)

S = set()
maxc = [0,0,0]
minc = [1000,1000,1000]

for l in sys.stdin:
    b = tuple(map(int,l.strip().split(',')))
    S.add(b)
    for i in range(3):
        maxc[i] = max(maxc[i],b[i])
        minc[i] = min(minc[i],b[i])

extarea = 0

V = set()

def is_inside(x):
    if not all(minc[i] <= x[i] <= maxc[i] for i in range(3)):
        return False
    for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        neighbor = (x[0]+d[0],x[1]+d[1],x[2]+d[2])
        if neighbor not in S and neighbor not in V:
            V.add(neighbor)
            if not is_inside(neighbor):
                return False
    return True

for x in S:
    for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        neighbor = (x[0]+d[0],x[1]+d[1],x[2]+d[2])
        V = set()
        if neighbor not in S and not is_inside(neighbor):
            extarea += 1

print("Part 2")
print(extarea)