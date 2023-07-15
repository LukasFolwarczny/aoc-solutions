# https://adventofcode.com/2021/day/2

import sys

instr = []

for line in sys.stdin:
    x = line.split()
    instr.append((x[0], int(x[1])))

horizontal = 0
depth = 0
aim = 0

for a,b in instr:
    match a:
        case "forward":
            horizontal += b
            depth += aim * b
        case "down":
            aim += b
        case "up":
            aim -= b

print(horizontal)
print(depth)

print("Part 2")
print(horizontal*depth)
