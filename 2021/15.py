# https://adventofcode.com/2021/day/15

import sys
import collections
from itertools import product

N = 0
M = []
bigM = []
mins = []
bigmins = []

diffs = [ (dr, ds) for dr in (1,0,-1) for ds in (1,0,-1) if dr == 0 or ds == 0 ]

for line in sys.stdin:
    N = len(line.strip())
    M.append(list(map(int,list(line.strip()))))
    mins.append([2**32]*N)

bigM = []

for i in range(5*N):
    bigM.append([0] * (5*N))
    bigmins.append([2**32] * (5*N))

for i, j, r, s in product(range(5), range(5), range(N), range(N)):
    bigM[r + i * N][s + j*N] = (M[r][s] - 1 + i + j) % 9 + 1


Q = collections.deque()
Q.append((0,0))
mins[0][0] = 0

while len(Q):
    (r,s) = Q.pop()
    for dr,ds in diffs:
        if 0 <= r+dr < N and 0 <= s+ds < N and mins[r][s] + M[r+dr][s+ds] < mins[r+dr][s+ds]:
            mins[r+dr][s+ds] = mins[r][s] + M[r+dr][s+ds]
            Q.appendleft((r+dr,s+ds))

print("Part 1")
print(mins[N-1][N-1])

Q = collections.deque()
Q.appendleft((0,0))
bigmins[0][0] = 0

while len(Q):
    (r,s) = Q.pop()
    for dr,ds in diffs:
        if 0 <= r+dr < 5*N and 0 <= s+ds < 5*N and bigmins[r][s] + bigM[r+dr][s+ds] < bigmins[r+dr][s+ds]:
            bigmins[r+dr][s+ds] = bigmins[r][s] + bigM[r+dr][s+ds]
            Q.appendleft((r+dr,s+ds))

print("Part 2")
print(bigmins[5*N-1][5*N-1])