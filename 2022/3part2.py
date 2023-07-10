# https://adventofcode.com/2022/day/3

import sys

s = 0
c = 0

C = set([])
 
for l in sys.stdin:
    B = set(l.strip())
    if c % 3 == 2:
       C = B & C
       x = C.pop()
       if ord(x) < ord('a'):
           s += ord(x) - ord('A') + 27
       else:
           s += ord(x) - ord('a') + 1
    elif c % 3 == 1:
       C = B & C
    else:
       C = B
    c += 1

print("Part 2")
print(s)
