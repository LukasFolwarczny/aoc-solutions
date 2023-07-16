# https://adventofcode.com/2021/day/11

import sys

M = []

steps = 100
dim = 10
flashes = 0

for line in sys.stdin:
    M.append(list(map(int,line.strip())))

for step in range(2**32):
    Q = []
    flashesold = flashes
    for r in range(dim):
        for s in range(dim):
            M[r][s] += 1
            if M[r][s] > 9:
                Q.append((r,s))
    while len(Q):
        flashes += 1
        (r,s) = Q.pop()
        for dr in (1,0,-1):
            for ds in (1,0,-1):
                newr = r+dr
                news = s+ds
                if (dr != 0 or ds != 0) and 0 <= newr < dim and 0 <= news < dim:
                    if M[newr][news] == 9:
                        Q.append((newr,news))
                    M[newr][news] += 1
    if flashes - flashesold == dim ** 2:
        print("Part 2")
        print(step + 1)
        break
    if step == 99:
        print("Part 1")
        print(flashes)

    for r in range(dim):
        for s in range(dim):
            if M[r][s] > 9:
                M[r][s] = 0