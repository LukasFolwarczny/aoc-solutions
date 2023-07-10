# https://adventofcode.com/2022/day/1

import sys

m = 0
a = 0

p = []

for l in sys.stdin:
    if l == '\n':
        m = max(m,a)
        p.append(a)
        a = 0
    else:
        a += int(l)

print("Part 1")
print(m)

print("Part 2")
p.sort()
print(p[-1] + p[-2] + p[-3])