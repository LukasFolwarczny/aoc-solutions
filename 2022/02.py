# https://adventofcode.com/2022/day/2

import sys
 
s = 0
t = 0

for l in sys.stdin:
    a,b = l.split()
    k1 = ord(a) - ord('A')
    k2 = ord(b) - ord('X') 

    s += 1 + k2
    if k1 == k2:
        s += 3
    elif (k1 + 1) % 3 == k2:
        s += 6

    if k2 == 0:
       t += (k1 + 2) % 3 + 1
    if k2 == 1:
       t += 3 + k1 + 1
    if k2 == 2:
       t += 6 + (k1 + 1) % 3 + 1

print("Part 1")
print(s)

print("Part 2")
print(t)
