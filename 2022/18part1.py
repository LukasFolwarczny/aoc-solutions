# https://adventofcode.com/2022/day/18

import sys

S = set()

for l in sys.stdin:
    S.add(tuple(map(int,l.strip().split(','))))

area = 0

for x in S:
    for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        if not (x[0]+d[0],x[1]+d[1],x[2]+d[2]) in S:
            area += 1

print("Part 1")
print(area)