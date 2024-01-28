# https://adventofcode.com/2022/day/6

import sys

N = 4

for line in sys.stdin:
    line = line.strip()
    for i in range(len(line) - N):
        if len(set(line[i : i + N])) == N:
            print(i + N)
            break
