# https://adventofcode.com/2022/day/24

import sys
from collections import deque

blizzards = []

R = 0  # Number of rows
C = 0  # Number of columns

for line in sys.stdin:
    C = len(line.strip())
    for c, symbol in enumerate(line.strip()):
        if symbol in ('<', '>', '^', 'v'):
            blizzards.append((R, c, symbol))
    R += 1


current_blizzard_positions = set()
current_t = 0


def is_free(r, c, t):
    global current_t, current_blizzard_positions
    if current_t != t:
        current_blizzard_positions = blizzard_positions(t)
        current_t = t
    return (r, c) not in current_blizzard_positions


def blizzard_positions(t):
    positions = set()
    for r, c, direction in blizzards:
        match direction:
            case '<':
                positions.add((r, (c - 1 - t) % (C - 2) + 1))
            case '>':
                positions.add((r, (t + c - 1) % (C - 2) + 1))
            case '^':
                positions.add(((r - 1 - t) % (R - 2) + 1, c))
            case 'v':
                positions.add(((t + r - 1) % (R - 2) + 1, c))
    return positions


initial_position = 0, 1
final_position = R - 1, C - 2
Q = deque([(0, 1, 0, 0)])  # (row coordinate, column coordinate, time, state)
V = {(0, 1, 0, 0)}  # visited configurations
part1_solved = False

while len(Q):
    r, c, t, state = Q.popleft()
    if (r, c) == final_position and state == 2:
        print('Part 2')
        print(t)
        break
    if not part1_solved and (r, c) == final_position and state == 1:
        print('Part 1')
        print(t)
        part1_solved = True
    for d_r, d_c in ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)):
        new_r, new_c = r + d_r, c + d_c
        if (
            1 <= new_r < R - 1
            or (new_r, new_c) in (initial_position, final_position)
        ) and (1 <= new_c < C - 1):
            new_state = state
            if state == 0 and (new_r, new_c) == final_position:
                new_state = 1
            elif state == 1 and (new_r, new_c) == initial_position:
                new_state = 2
            if (
                is_free(new_r, new_c, t + 1)
                and (to_add := (new_r, new_c, t + 1, new_state)) not in V
            ):
                V.add(to_add)
                Q.append(to_add)
