# https://adventofcode.com/2022/day/4

import sys

sum_ = 0

for line in sys.stdin:
    A, B = line.split(',')
    a = A.split('-')
    A1 = int(a[0])
    A2 = int(a[1])
    b = B.split('-')
    B1 = int(b[0])
    B2 = int(b[1])
    if not (A2 < B1 or A1 > B2):
        sum_ += 1

print(sum_)
