# https://adventofcode.com/2022/day/12

import sys
from collections import deque

start = destination = (0, 0)
M = []

for i, line in enumerate(sys.stdin):
    row = []
    for j, c in enumerate(line):
        match c:
            case '\n':
                pass
            case 'S':
                start = (i, j)
                row.append(0)
            case 'E':
                destination = (i, j)
                row.append(25)
            case _:
                row.append(ord(c) - ord('a'))
    M.append(row)

R = len(M)
C = len(M[0])

V = [[-1] * C for _ in range(R)]

Q = deque()

V[destination[0]][destination[1]] = 0
Q.appendleft(destination)

while len(Q):
    v = Q.pop()
    for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        new_v = (v[0] + direction[0], v[1] + direction[1])
        if (
            0 <= new_v[0] < R
            and 0 <= new_v[1] < C
            and M[new_v[0]][new_v[1]] - M[v[0]][v[1]] >= -1
            and V[new_v[0]][new_v[1]] == -1
        ):
            V[new_v[0]][new_v[1]] = V[v[0]][v[1]] + 1
            Q.appendleft(new_v)
            if M[new_v[0]][new_v[1]] == 0:
                print(V[new_v[0]][new_v[1]])
                exit()
