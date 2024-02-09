# https://adventofcode.com/2022/day/23

import sys
from collections import Counter
from itertools import count

ROUNDS = 10

ADJACENT = {
    (-1, 0): [(-1, 0), (-1, 1), (-1, -1)],
    (1, 0): [(1, 0), (1, -1), (1, 1)],
    (0, -1): [(0, -1), (1, -1), (-1, -1)],
    (0, 1): [(0, 1), (1, 1), (-1, 1)],
}


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Initially: N, S, W, E
elves = set()

for r, line in enumerate(sys.stdin):
    for c, symbol in enumerate(line.strip()):
        if symbol == '#':
            elves.add((r, c))

for round in count():
    actions = {}
    for elf in elves:
        actions[elf] = elf
        if any(
            (elf[0] + d_r, elf[1] + d_c) in elves
            for d_r in (-1, 0, 1)
            for d_c in (-1, 0, 1)
            if d_r != 0 or d_c != 0
        ):
            for direction in directions:
                if all(
                    (elf[0] + d[0], elf[1] + d[1]) not in elves
                    for d in ADJACENT[direction]
                ):
                    actions[elf] = (
                        elf[0] + direction[0],
                        elf[1] + direction[1],
                    )
                    break
    actions_multiset = Counter(actions.values())
    for elf in elves:
        if actions_multiset[actions[elf]] > 1:
            actions[elf] = elf

    if all(a == b for a, b in actions.items()):
        print('Part 2')
        print(round + 1)
        sys.exit()

    elves = set(actions.values())

    if round == 9:
        min_r = min(elf[0] for elf in elves)
        max_r = max(elf[0] for elf in elves)
        min_c = min(elf[1] for elf in elves)
        max_c = max(elf[1] for elf in elves)
        print('Part 1')
        print((max_r - min_r + 1) * (max_c - min_c + 1) - len(elves))

    directions.append(directions.pop(0))
