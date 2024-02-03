# https://adventofcode.com/2022/day/15

import sys

special_y = 2_000_000

sensors = []
beacons = []

for line in sys.stdin:
    splitted = line.split()
    s_x = int(splitted[2].split('=')[1].split(',')[0])
    s_y = int(splitted[3].split('=')[1].split(':')[0])
    b_x = int(splitted[8].split('=')[1].split(',')[0])
    b_y = int(splitted[9].split('=')[1])
    sensors.append((s_x, s_y))
    beacons.append((b_x, b_y))

if len(sensors) < 30:  # Test case has different `special_y` than real inputs
    special_y = 10

min_x = min(x for x, _ in sensors + beacons)
max_x = max(x for x, _ in sensors + beacons)
min_y = min(y for _, y in sensors + beacons)
max_y = max(y for _, y in sensors + beacons)

M = set()

for (b_x, b_y), (s_x, s_y) in zip(beacons, sensors):
    dist = abs(b_x - s_x) + abs(b_y - s_y)
    dist_y = abs(s_y - special_y)
    if dist_y <= dist:
        for j in range(dist - dist_y + 1):
            M.add((s_x + j, special_y))
            M.add((s_x - j, special_y))

M -= set(beacons)

count = sum([1 for _, y in M if y == special_y])

print(count)
