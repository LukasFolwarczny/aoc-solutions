# https://adventofcode.com/2020/day/9

import sys

L = [ int(line) for line in sys.stdin ]

key = 25
if len(L) < 30:
    key = 5

invald = -1

for i in range(key,len(L)):
    if not any(L[j] + L[k] == L[i] for j in range(i-key,i) for k in range(j+1,i)):
        print("Part 1")
        print(L[i])
        invalid = i
        break

for a in range(len(L)):
    s = L[a]
    for b in range(a+1,len(L)):
        s += L[b]
        if s == L[invalid]:
            print("Part 2")
            print(max(L[a:b+1]) + min(L[a:b+1]))