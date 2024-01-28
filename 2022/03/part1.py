# https://adventofcode.com/2022/day/3

import sys

priority_sum = 0

for line in sys.stdin:
    half = (len(line) - 1) // 2
    a = set(line[:half])
    b = set(line[half:])
    c = a & b
    x = ord(c.pop())
    if x < ord('a'):
        priority_sum += x - ord('A') + 27
    else:
        priority_sum += x - ord('a') + 1

print(priority_sum)
