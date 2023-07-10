# https://adventofcode.com/2022/day/15
# Runs in 0.06 seconds on my laptop and my contest input, but I am not entirely sure about the correctness.

import sys
import math

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
B = set(beacons)
D = []
for i in range(L):
    D.append(abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1]))
    
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def is_inside(p,i):
    return dist(p,sensors[i]) <= D[i]

def ball_sortof_intersec(i,j):
    if D[i] + D[j] < dist(sensors[i],sensors[j]):
        return []
    L = []
    for ddx in (-1,1):
        for ddy in (-1,1):
            for ddxa in (-1,1):
                for ddya in (-1,1):
                    p1 = (sensors[i][0] + ddx*D[i], sensors[i][1])
                    p2 = (sensors[i][0], sensors[i][1] + ddy*D[i])
                    q1 = (sensors[j][0] + ddxa*D[j], sensors[j][1])
                    q2 = (sensors[j][0], sensors[j][1] + ddya*D[j])
                    inter = line_intersec(p1,p2,q1,q2)
                    if math.floor(inter[0]) == inter[0]:
                        L.append((int(inter[0]+1),int(inter[1])))
                        L.append((int(inter[0]-1),int(inter[1])))
                        L.append((int(inter[0]),int(inter[1]+1)))
                        L.append((int(inter[0]),int(inter[1]-1)))
                    else:
                        L.append((int(inter[0]+0.5),int(inter[1]+0.5)))
                        L.append((int(inter[0]-0.5),int(inter[1]+0.5)))
                        L.append((int(inter[0]-0.5),int(inter[1]-0.5)))
                        L.append((int(inter[0]+0.5),int(inter[1]-0.5)))
    return L

# Formula from
# https://en.wikipedia.org/wiki/Line–line_intersection
def line_intersec(p1,p2,q1,q2):
    xden = (p1[0]*p2[1] - p1[1]*p2[0])*(q1[0] - q2[0]) - (p1[0] - p2[0])*(q1[0]*q2[1] - q1[1]*q2[0])
    xnom = (p1[0] - p2[0])*(q1[1] - q2[1]) - (p1[1] - p2[1])*(q1[0] - q2[0])
    yden = (p1[0]*p2[1] - p1[1]*p2[0])*(q1[1] - q2[1]) - (p1[1] - p2[1])*(q1[0]*q2[1] - q1[1]*q2[0])
    ynom = (p1[0] - p2[0])*(q1[1] - q2[1]) - (p1[1] - p2[1])*(q1[0] - q2[0])
    if xnom == 0 or ynom == 0:
        return (0,0)
    return (xden/xnom,yden/ynom)


for i in range(L):
    for j in range(i+1,L):
        sez = ball_sortof_intersec(i,j)
        good = [ all(not is_inside(s,k) for k in range(L)) for s in sez]
        for s in range(len(sez)):
            if good[s] and 0 <= sez[s][0] < special_x and 0 <= sez[s][1] < special_x:
                print(sez[s])
                print("Part 2")
                print(4_000_000*sez[s][0] + sez[s][1])
                exit()