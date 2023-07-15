# https://adventofcode.com/2021/day/1

import sys

prev = -1

ans = 0

for line in sys.stdin:
    if prev != -1 and int(line) > prev:
        ans = ans + 1
    prev = int(line)

print("Part 1")
print(ans)


