# https://adventofcode.com/2022/day/17

import sys

instructions = sys.stdin.readline().strip()
iterations = 2022

shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]
fallen = set()


def is_down(shape, pos):
    for x in shape:
        if x[0] + pos[0] == 0 or (x[0] + pos[0] - 1, x[1] + pos[1]) in fallen:
            return True
    return False


def move_left(shape, pos):
    for x in shape:
        if x[1] + pos[1] == 0 or (x[0] + pos[0], x[1] + pos[1] - 1) in fallen:
            return pos
    return (pos[0], pos[1] - 1)


def move_right(shape, pos):
    for x in shape:
        if x[1] + pos[1] == 6 or (x[0] + pos[0], x[1] + pos[1] + 1) in fallen:
            return pos
    return (pos[0], pos[1] + 1)


top = -1
p = 0

for i in range(iterations):
    shape = shapes[i % 5]
    pos = (top + 4, 2)
    while True:
        instr = instructions[p % len(instructions)]
        p += 1
        if instr == '<':
            pos = move_left(shape, pos)
        else:
            pos = move_right(shape, pos)
        if is_down(shape, pos):
            break
        else:
            pos = (pos[0] - 1, pos[1])
    for x in shape:
        fallen.add((pos[0] + x[0], pos[1] + x[1]))
        top = max(top, pos[0] + x[0])

print(top + 1)
