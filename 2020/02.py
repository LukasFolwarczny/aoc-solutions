# https://adventofcode.com/2020/day/2

import sys

count = 0
count2 = 0

for line in sys.stdin:
    ll = line.strip().split()
    pwd = ll[2]
    char = ll[1][0]
    a = int(ll[0].split('-')[0])
    b = int(ll[0].split('-')[1])
    if a <= list(pwd).count(char) <= b:
        count += 1
    if (pwd[a-1] == char) != (pwd[b-1] == char):
        count2 += 1

print("Part 1")
print(count)
print("Part 2")
print(count2)