# https://adventofcode.com/2021/day/7

import sys
import math

a = list(map(int,sys.stdin.readline().split(',')))

m = max(a)

opt1 = 2**32
opt2 = 2**32

for i in range(m+1):
    opt1 = min(opt1, sum ( abs(i-j) for j in a))
    opt2 = min(opt2, sum ( abs(i-j) * (abs(i-j) + 1) // 2 for j in a))

print("Part 1")
print(opt1)
print("Part 2")
print(opt2)