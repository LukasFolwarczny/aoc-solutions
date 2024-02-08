# https://adventofcode.com/2022/day/22

import sys

from more_itertools import split_at

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
M = []
instructions = []

while (line := sys.stdin.readline()) != '\n':
    M.append(line[:-1])

instr_line = sys.stdin.readline().strip()

for chunk in split_at(
    instr_line, lambda c: c in ('L', 'R'), keep_separator=True
):
    chunk_list = list(chunk)
    if chunk_list[0] in ('L', 'R'):
        instructions.append(chunk_list[0])
    else:
        instructions.append(int(''.join(chunk_list)))


R = len(M)  # number of rows
C = max(len(row) for row in M)  # number of columns

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
            if d_r == 0:
                new_r = r
                if left_bounds[r] <= c + d_c <= right_bounds[r]:
                    new_c = c + d_c
                elif d_c == -1:
                    new_c = right_bounds[r]
                elif d_c == 1:
                    new_c = left_bounds[r]
            elif d_c == 0:
                new_c = c
                if top_bounds[c] <= r + d_r <= bottom_bounds[c]:
                    new_r = r + d_r
                elif d_r == 1:
                    new_r = top_bounds[c]
                elif d_r == -1:
                    new_r = bottom_bounds[c]
            if M[new_r][new_c] == '.':
                r, c = new_r, new_c
            else:
                break

print((r + 1) * 1000 + (c + 1) * 4 + direction)
