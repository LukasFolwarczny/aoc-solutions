# https://adventofcode.com/2021/day/1

import sys

arr = [ int(s) for s in sys.stdin.readlines() ]
    
prev = -1
ans = 0
for i in range(2,len(arr)):
    val = sum(arr[i-2:i+1])
    if prev != -1 and prev < val:
        ans = ans + 1
    prev = val

print("Part 2")
print(ans)