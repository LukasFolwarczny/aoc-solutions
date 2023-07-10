# https://adventofcode.com/2022/day/8

import sys

s = 0

xM = sys.stdin.readlines()
R = len(xM)
S = len(xM[0]) - 1
M = []

M = [ [ int(xM[i][j]) for j in range(S) ] for i in range(R) ]

def mymax(l):
    if len(l) == 0:
        return -1
    return max(l)

ms = -1

for i in range(R):
    for j in range(S):
        h = M[i][j]

        if mymax([M[i1][j] for i1 in range(i)]) < h or \
            mymax([M[i1][j] for i1 in range(i+1,R)]) < h or \
            mymax([M[i][j1] for j1 in range(j)]) < h or \
            mymax([M[i][j1] for j1 in range(j+1,S)]) < h:
           s += 1

        l = 1
        for dd in ((0,1), (0,-1), (1,0), (-1,0)):
            ix, jx = i, j
            while 0 <= ix + dd[0] < R and 0 <= jx + dd[1] < S and M[ix + dd[0]][jx + dd[1]] < h:
                ix += dd[0]
                jx += dd[1]
            if 0 <= ix + dd[0] < R and 0 <= jx + dd[1] < S:
                ix += dd[0]
                jx += dd[1]
            l *= ix - i + jx - j
        ms = max(ms,l)


print("Part 1")
print(s)
print("Part 2")
print(ms)