# https://adventofcode.com/2022/day/8

import sys
from functools import partial

M = [[int(c) for c in row.strip()] for row in sys.stdin if not row.isspace()]
X = len(M)  # number of rows
Y = len(M[0])  # number of columns

my_max = partial(max, default=-1)

result = sum(
    1
    for x in range(X)
    for y in range(Y)
    if min(
        my_max([M[x1][y] for x1 in range(x)]),
        my_max([M[x1][y] for x1 in range(x + 1, X)]),
        my_max([M[x][y1] for y1 in range(y)]),
        my_max([M[x][y1] for y1 in range(y + 1, Y)]),
    )
    < M[x][y]
)

print(result)
