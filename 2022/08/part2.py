# https://adventofcode.com/2022/day/8

import sys

from lib import Vec2D

M = [[int(x) for x in row.strip()] for row in sys.stdin if not row.isspace()]
X = len(M)  # number of rows
Y = len(M[0])  # number of columns

result = -1


def is_inside(v):
    return 0 <= v.x < X and 0 <= v.y < Y


for x in range(X):
    for y in range(Y):
        h = M[x][y]
        scenic_score = 1
        for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            position = Vec2D(x, y)
            while (
                is_inside(position + direction)
                and M[(position + direction).x][(position + direction).y] < h
            ):
                position += direction
            if is_inside(position + direction):
                position += direction
            scenic_score *= position.x - x + position.y - y
        result = max(result, scenic_score)

print(result)
