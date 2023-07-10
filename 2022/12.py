# https://adventofcode.com/2022/day/12

import sys
import collections

steps = 0

start = destination = (0,0)

M = []
R = S = 0

dirs = ((0,1),(1,0),(0,-1),(-1,0))


lines = sys.stdin.readlines()

for i,l in enumerate(lines):
    line = []
    for j,c in enumerate(l):
        if c != "\n":
            if c == "S":
                start = (i,j)
                line.append(0)
            elif c == "E":  
                destination = (i,j)
                line.append(25)
            else:
                line.append(ord(c) - ord('a'))
    M.append(line)
    S = len(line)
R = len(M)

V = [[-1 for _ in range(S)] for _ in range(R)]

mindist = 2**30

Q = collections.deque()

for r in range(R):
    for s in range(S):
        if M[r][s] == 0:
            for rr in range(R):
                for ss in range(S):
                    V[rr][ss] = -1
            V[r][s] = 0
            Q.clear()
            Q.appendleft((r,s))

            while len(Q):
                v = Q.pop()
                for d in dirs:
                    newv = (v[0]+d[0],v[1]+d[1])
                    if 0 <= newv[0] < R and 0 <= newv[1] < S and M[newv[0]][newv[1]] - M[v[0]][v[1]] <= 1 and \
                    V[newv[0]][newv[1]] == -1:
                        V[newv[0]][newv[1]] = V[v[0]][v[1]] + 1
                        Q.appendleft(newv)
            if V[destination[0]][destination[1]] != -1:
                mindist = min(mindist, V[destination[0]][destination[1]])
            if (r,s) == start:
                print("Part 1")
                print(V[destination[0]][destination[1]])

print("Part 2")
print(mindist)