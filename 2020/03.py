# https://adventofcode.com/2020/day/3

import sys

M = [ line.strip() for line in sys.stdin ]

R = len(M)
S = len(M[0])

prod = 1

for step in (1,3,5,7):
    count = 0
    s = 0
    for r in range(R):
        if M[r][s] == '#':
            count += 1
        s = (s + step) % S

    if step == 3:
        print("Part 1")
        print(count)
    prod *= count

r = 0
s = 0
count = 0

while r < R:
    if M[r][s] == '#':
        count += 1
    r = r + 2
    s = (s + 1) % S

prod *= count
print("Part 2")
print(prod)