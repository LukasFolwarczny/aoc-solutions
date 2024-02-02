# https://adventofcode.com/2022/day/10

import sys

X = 1
cycle = 1


def update():
    if (cycle - 1) % 40 in (X - 1, X, X + 1):
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0:
        print()


for line in sys.stdin:
    update()
    cycle += 1
    if line[0] == 'a':
        update()
        cycle += 1
        X += int(line.split()[1])
