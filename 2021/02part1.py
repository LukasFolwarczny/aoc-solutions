# https://adventofcode.com/2021/day/2

import sys

instr = []

for line in sys.stdin:
    x = line.split()
    instr.append((x[0], int(x[1])))

horizontal = 0
depth = 0

for a,b in instr:
    match a:
        case "forward":
            horizontal += b
        case "down":
            depth += b
        case "up":
            depth -= b

print(horizontal)
print(depth)
print("Part 1")
print(horizontal*depth)
