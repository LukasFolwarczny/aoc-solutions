# https://adventofcode.com/2022/day/15
# Runs in 0.06 seconds on my laptop and my contest input, but I am not entirely
# sure about the correctness.

import math
import sys
from itertools import product


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Formula from
# https://en.wikipedia.org/wiki/Line–line_intersection
def line_intersec(p1, p2, q1, q2):
    xden = (p1[0] * p2[1] - p1[1] * p2[0]) * (q1[0] - q2[0]) - (
        p1[0] - p2[0]
    ) * (q1[0] * q2[1] - q1[1] * q2[0])
    xnom = (p1[0] - p2[0]) * (q1[1] - q2[1]) - (p1[1] - p2[1]) * (
        q1[0] - q2[0]
    )
    yden = (p1[0] * p2[1] - p1[1] * p2[0]) * (q1[1] - q2[1]) - (
        p1[1] - p2[1]
    ) * (q1[0] * q2[1] - q1[1] * q2[0])
    ynom = (p1[0] - p2[0]) * (q1[1] - q2[1]) - (p1[1] - p2[1]) * (
        q1[0] - q2[0]
    )
    if xnom == 0 or ynom == 0:
        return (0, 0)
    return (xden / xnom, yden / ynom)


bound = 4_000_000

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

if len(sensors) < 30:  # Test case has different `bound` than real inputs
    bound = 20

min_x = min(x for x, _ in sensors + beacons)
max_x = max(x for x, _ in sensors + beacons)
min_y = min(y for _, y in sensors + beacons)
max_y = max(y for _, y in sensors + beacons)

D = [dist(sensor, beacon) for sensor, beacon in zip(sensors, beacons)]


def is_inside(p, i):
    return dist(p, sensors[i]) <= D[i]


def ball_sortof_intersec(i, j):
    if D[i] + D[j] < dist(sensors[i], sensors[j]):
        return []
    L = []
    for dd_x, dd_y, dd2_x, dd2_y in product((-1, 1), repeat=4):
        p1 = (sensors[i][0] + dd_x * D[i], sensors[i][1])
        p2 = (sensors[i][0], sensors[i][1] + dd_y * D[i])
        q1 = (sensors[j][0] + dd2_x * D[j], sensors[j][1])
        q2 = (sensors[j][0], sensors[j][1] + dd2_y * D[j])
        intersec = line_intersec(p1, p2, q1, q2)
        if math.floor(intersec[0]) == intersec[0]:
            L.append((int(intersec[0] + 1), int(intersec[1])))
            L.append((int(intersec[0] - 1), int(intersec[1])))
            L.append((int(intersec[0]), int(intersec[1] + 1)))
            L.append((int(intersec[0]), int(intersec[1] - 1)))
        else:
            L.append((int(intersec[0] + 0.5), int(intersec[1] + 0.5)))
            L.append((int(intersec[0] - 0.5), int(intersec[1] + 0.5)))
            L.append((int(intersec[0] - 0.5), int(intersec[1] - 0.5)))
            L.append((int(intersec[0] + 0.5), int(intersec[1] - 0.5)))
    return L


N = len(sensors)

for i in range(N):
    for j in range(i + 1, N):
        for x, y in ball_sortof_intersec(i, j):
            if (
                all(not is_inside((x, y), k) for k in range(N))
                and 0 <= x < bound
                and 0 <= y < bound
            ):
                print(4_000_000 * x + y)
                exit()
