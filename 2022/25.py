# https://adventofcode.com/2022/day/25

import sys

snafu_to_std = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
std_to_snafu = {}

for x,y in snafu_to_std.items():
    std_to_snafu[y] = x

sum = 0

for line in sys.stdin:
    num = 0
    for c in line.strip():
        num = num * 5 + snafu_to_std[c]
    sum += num

def convert_to_snafu(x):
    r = ''
    while x != 0:
        remainder = x % 5
        if remainder > 2:
            remainder -= 5
        r = std_to_snafu[remainder] + r
        x -= remainder
        x //= 5
    return r


print('Part 1')
print(convert_to_snafu(sum))