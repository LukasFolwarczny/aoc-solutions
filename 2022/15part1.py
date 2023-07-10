# https://adventofcode.com/2022/day/15

import sys

special_y = 2_000_000

maxx = -2**32
maxy = -2**32
minx = 2**32
miny = 2**32


sensors = []
beacons = []

for l in sys.stdin:
    ll = l.split()
    sx = int(ll[2].split("=")[1].split(",")[0])
    sy = int(ll[3].split("=")[1].split(":")[0])
    bx = int(ll[8].split("=")[1].split(",")[0])
    by = int(ll[9].split("=")[1])
    maxx = max(maxx,sx,bx)
    maxy = max(maxy,sy,by)
    minx = min(minx,sx,bx)
    miny = min(miny,sy,by)
    sensors.append((sx,sy))
    beacons.append((bx,by))

if len(sensors) < 30:
    special_y = 10

print(maxx, maxy)

M = set()

for i,sensor in enumerate(sensors):
    dist = abs(sensor[0] - beacons[i][0]) + abs(sensor[1] - beacons[i][1])
    disty = abs(sensor[1] - special_y)
    if disty <= dist:
        for j in range(dist-disty+1):
            M.add((sensor[0] + j, special_y))
            M.add((sensor[0] - j, special_y))


for b in beacons:
    if b in M:
        M.remove(b)

count = sum([1 for m in M if m[1] == special_y])

print("Part 1")
print(count)