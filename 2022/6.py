# https://adventofcode.com/2022/day/6

import sys

l = sys.stdin.readline()

p1s = False

for i in range(len(l)-4):
    if not p1s and len(set(l[i:i+4])) == 4:
        p1s = True
        print("Part 1")
        print(i + 4)
    if len(set(l[i:i+14])) == 14:
        print("Part 2")
        print(i + 14)
        break