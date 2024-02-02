# https://adventofcode.com/2022/day/10

import sys

X = 1
sum_ = 0
cycle = 1


def update():
    global sum_
    if cycle in range(20, 221, 40):
        sum_ += X * cycle


for line in sys.stdin:
    update()
    cycle += 1
    if line[0] == 'a':
        update()
        cycle += 1
        X += int(line.split()[1])

print(sum_)
