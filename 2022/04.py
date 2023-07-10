# https://adventofcode.com/2022/day/4

import sys

s = 0
t = 0
 
for l in sys.stdin:
    A,B = l.split(',')
    a = A.split('-')
    A1 = int(a[0])
    A2 = int(a[1])
    b = B.split('-')
    B1 = int(b[0])
    B2 = int(b[1])
    if (A1 <= B1 and A2 >= B2) or (A1 >= B1 and A2 <= B2):
        s += 1
    if not (A2 < B1 or A1 > B2):
        t += 1

print("Part 1")
print(s)
print("Part 2")
print(t)
