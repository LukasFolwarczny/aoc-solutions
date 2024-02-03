# https://adventofcode.com/2022/day/14

import sys
from itertools import pairwise


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def parse_pair(pair):
    a, b = pair.split(',')
    return int(a), int(b)


lines = [[parse_pair(pair) for pair in line.split('->')] for line in sys.stdin]

max_y = max(y for line in lines for _, y in line)

sand = set()

for line in lines:
    for (p_x, p_y), (q_x, q_y) in pairwise(line):
        d_x, d_y = sgn(q_x - p_x), sgn(q_y - p_y)
        while (p_x, p_y) != (q_x, q_y):
            sand.add((p_x, p_y))
            p_x += d_x
            p_y += d_y
        sand.add((q_x, q_y))

bound = max_y + 2


def fall():
    p_x, p_y = 500, 0
    if (p_x, p_y) in sand:
        return False
    while p_y < bound - 1:
        if (p_x, p_y + 1) in sand:
            if (p_x - 1, p_y + 1) not in sand:
                p_x -= 1
                p_y += 1
            elif (p_x + 1, p_y + 1) not in sand:
                p_x += 1
                p_y += 1
            else:
                sand.add((p_x, p_y))
                return True
        else:
            p_y += 1
    sand.add((p_x, p_y))
    return True


fallen = 0
while fall():
    fallen += 1

print(fallen)
