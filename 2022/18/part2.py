# https://adventofcode.com/2022/day/18

import sys

sys.setrecursionlimit(10_000)

DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

cubes = {tuple(int(x) for x in line.split(',')) for line in sys.stdin}

min_coords = tuple(min(cube[d] for cube in cubes) for d in range(3))
max_coords = tuple(max(cube[d] for cube in cubes) for d in range(3))


def is_inside(cube, visited):
    if not all(min_coords[d] <= cube[d] <= max_coords[d] for d in range(3)):
        return False
    for d_x, d_y, d_z in DIRECTIONS:
        neighbor = (cube[0] + d_x, cube[1] + d_y, cube[2] + d_z)
        if neighbor not in cubes and neighbor not in visited:
            visited.add(neighbor)
            if not is_inside(neighbor, visited):
                return False
    return True


exterior_area = 0

for x, y, z in cubes:
    for d_x, d_y, d_z in DIRECTIONS:
        neighbor = (x + d_x, y + d_y, z + d_z)
        if neighbor not in cubes and not is_inside(neighbor, set()):
            exterior_area += 1

print(exterior_area)
