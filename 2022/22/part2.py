# https://adventofcode.com/2022/day/22

# Unfortunately, this only works for my particular input.

import sys

from more_itertools import split_at

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def identify_face(r, c):
    if r < 50:
        if 50 <= c < 100:
            return 0
        if 100 <= c < 150:
            return 1
    if 50 <= r < 100:
        return 2
    if 100 <= r < 150:
        if 0 <= c < 50:
            return 3
        if 50 <= c < 100:
            return 4
    if 150 <= r < 200:
        return 5
    raise Exception(r, c)


def jump(r, c, direction):
    face = identify_face(r, c)
    if direction == 0:
        if face == 1:
            return 49 - r + 100, c - 50, 2
        if face == 2:
            return 49, r, 3
        if face == 4:
            return 49 - (r - 100), 149, 2
        if face == 5:
            return 149, r - 100, 3
    if direction == 1:
        if face == 1:
            return c - 50, 99, 2
        if face == 4:
            return c + 100, 49, 2
        if face == 5:
            return 0, c + 100, 1
    if direction == 2:
        if face == 0:
            return 149 - r, 0, 0
        if face == 2:
            return 100, r, 1
        if face == 3:
            return 50, 149 - r, 0
        if face == 5:
            return 0, r - 100, 1
    if direction == 3:
        if face == 0:
            return c + 100, 0, 0
        if face == 1:
            return 199, c - 100, 3
        if face == 3:
            return c + 50, 50, 0
    raise Exception(r, c, direction)


M = []
instructions = []

while (line := sys.stdin.readline()) != '\n':
    M.append(line[:-1])

instr_line = sys.stdin.readline()

for chunk in split_at(
    instr_line, lambda c: c in ('L', 'R'), keep_separator=True
):
    chunk_list = list(chunk)
    if chunk_list[0] in ('L', 'R'):
        instructions.append(chunk_list[0])
    else:
        instructions.append(int(''.join(chunk_list)))


R = len(M)  # number of rows
C = max([len(row) for row in M])  # number of columns

left_bounds = [
    min(c for c in range(C) if c < len(M[r]) and M[r][c] in ('.', '#'))
    for r in range(R)
]
right_bounds = [len(M[r]) - 1 for r in range(R)]
top_bounds = [
    min(r for r in range(R) if c < len(M[r]) and M[r][c] in ('.', '#'))
    for c in range(C)
]
bottom_bounds = [
    max(r for r in range(R) if c < len(M[r]) and M[r][c] in ('.', '#'))
    for c in range(C)
]

r, c = 0, left_bounds[0]  # current position
direction = 0

for instruction in instructions:
    if instruction == 'L':
        direction = (direction - 1) % 4
    elif instruction == 'R':
        direction = (direction + 1) % 4
    else:
        for step in range(instruction):
            d_r, d_c = DIRECTIONS[direction]
            if (
                left_bounds[r] <= c + d_c <= right_bounds[r]
                and top_bounds[c] <= r + d_r <= bottom_bounds[c]
            ):
                new_r, new_c, new_direction = r + d_r, c + d_c, direction
            else:
                new_r, new_c, new_direction = jump(r, c, direction)
            if M[new_r][new_c] == '.':
                r, c, direction = new_r, new_c, new_direction
            else:
                break

print((r + 1) * 1000 + (c + 1) * 4 + direction)
