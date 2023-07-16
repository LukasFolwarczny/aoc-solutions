# https://adventofcode.com/2021/day/14

import sys

start = sys.stdin.readline().strip()
sys.stdin.readline()

D = {}

for line in sys.stdin:
    ll = line.strip().split(" -> ")
    D[(ll[0][0],ll[0][1])] = ll[1]

x = list(start)

for step in range(10):
    y = [x[0]]
    for i in range(len(x) - 1):
        key = (x[i],x[i+1])
        if key in D:
            y.append(D[key])
        y.append(x[i+1])
    x = y

counter = {}

for c in x:
    if c not in counter:
        counter[c] = 0
    counter[c] += 1

minc = min(counter.values())
maxc = max(counter.values())
print("Part 1")
print(maxc - minc)