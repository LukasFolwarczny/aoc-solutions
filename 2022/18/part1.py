# https://adventofcode.com/2022/day/18

import sys

cubes = {tuple(int(x) for x in line.split(',')) for line in sys.stdin}

surface_area = 0

for x, y, z in cubes:
    for d_x, d_y, d_z in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        if (x + d_x, y + d_y, z + d_z) not in cubes:
            surface_area += 1

print(surface_area)
