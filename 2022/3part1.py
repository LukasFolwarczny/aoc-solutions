# https://adventofcode.com/2022/day/3

import sys

s = 0
 
for l in sys.stdin:
    p = (len(l)-1)//2
    a = set(l[:p])
    b = set(l[p:])
    c = a & b
    x = c.pop()
    if ord(x) < ord('a'):
        s += ord(x) - ord('A') + 27
    else:
        s += ord(x) - ord('a') + 1

print("Part 1")
print(s)
