# https://adventofcode.com/2021/day/9

import sys
import math

low_points_val = 0
areas = []
area = -1


xM = sys.stdin.readlines()
R = len(xM)
C = len(xM[0]) - 1
M = [ [ int(xM[r][c]) for r in range(R) ] for c in range(C) ]
V = [ [ M[r][c] == 9 for r in range(R) ] for c in range(C) ] # visited

def BFS(r,c):
    global V
    V[r][c] = True
    global area
    area += 1
    if r > 0 and not V[r-1][c]:
       BFS(r-1,c) 
    if c > 0 and not V[r][c-1]:
       BFS(r,c-1) 
    if r < R-1 and not V[r+1][c]:
       BFS(r+1,c) 
    if c < C-1 and not V[r][c+1]:
       BFS(r,c+1) 

for r in range(R):
    for c in range(C):
        v = M[r][c]
        l = True
        if r > 0 and M[r-1][c] <= v: l = False
        if c > 0 and M[r][c-1] <= v: l = False
        if r < R-1 and M[r+1][c] <= v: l = False
        if c < C-1 and M[r][c+1] <= v: l = False
        if l: low_points_val += v + 1

for r in range(R):
    for c in range(C):
        if not V[r][c]:
            area = 0
            BFS(r,c)
            areas.append(area)

print("Part 1")
print(low_points_val)

areas.sort()
print("Part 2")
print(math.prod(areas[-3:]))