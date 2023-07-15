# https://adventofcode.com/2021/day/8

import sys

s = 0

for l in sys.stdin:
    lx = l.strip().split("|")[1].split(" ")
    s += sum(1 for x in lx if len(x) in (2, 3, 4, 7))

print("Part 1")
print(s)