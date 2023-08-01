# https://adventofcode.com/2020/day/10

import sys

L = sorted(int(line) for line in sys.stdin)

D = [0] * 4
D[L[0]] = 1

for i in range(1,len(L)):
    D[L[i] - L[i-1]] += 1

D[3] += 1

print("Part 1")
print(D[1] * D[3])

dyn = {}

def f(i):
    if i == len(L) - 1:
        return 1
    if i in dyn.keys():
        return dyn[i]
    res = 0
    for j in range(i+1,len(L)):
        if L[j] - L[i] <= 3:
            res += f(j)
        else:
            break
    dyn[i] = res
    return res

total = 0
for j, e in enumerate(L):
    if e <= 3:
        total += f(j)
    else:
        break

print("Part 2")
print(total)