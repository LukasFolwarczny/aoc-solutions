# https://adventofcode.com/2022/day/15
# Runs in 22 seconds on my laptop and my contest input.

import sys

special_y = 2_000_000
special_x = 4_000_000

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
    special_x = 20

L = len(sensors)

D = []
for i in range(L):
    D.append(abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1]))

def mykey(a):
    return a[0]
    
def uncovered(Li):
    li = len(Li)
    Li.sort(key=mykey)
    y = -2**31
    if Li[0][0] > 0:
        return Li[0][0]-1
    else:
        y = Li[0][1]
        for i in range(li-1):
            if y+1 < Li[i+1][0]:
                return y+1
            y = max(y,Li[i+1][1])
    if y <= special_x:
        return y-1
    return -1

for x in range(special_x):
    if x%100_000==0:
        print(x)
    Y = []
    for i in range(L):
        if abs(x - sensors[i][0]) <= D[i]:
            Y.append((sensors[i][1] - D[i] + abs(x - sensors[i][0]),sensors[i][1] + D[i] - abs(x - sensors[i][0])))
    y = uncovered(Y)
    if y >= 0:
        print((x,y))
        print("Part 2")
        print(x*4_000_000+y)
        break