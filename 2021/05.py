# https://adventofcode.com/2021/day/5

import sys
import math

lines = []

for y in sys.stdin:
    z = y.split()
    z1,z2 = z[0].split(','),z[2].split(',')
    lines.append( ( (int(z1[0]), int(z1[1])), (int(z2[0]), int(z2[1])) ) )

D1 = {}
D2 = {}

def add_D1(p):
    if p in D1:
        D1[p] += 1
    else:
        D1[p] = 1

def add_D2(p):
    if p in D2:
        D2[p] += 1
    else:
        D2[p] = 1

for l in lines:
    a = l[0]
    b = l[1]
    d = (a[0] - b[0], a[1] - b[1])
    g = math.gcd(d[0], d[1])
    dd = (d[0] // g, d[1] // g)
    for i in range(g + 1):
        if a[1] == b[1] or a[0] == b[0]:
            add_D1( (b[0] + i*dd[0], b[1] + i*dd[1]) )
        add_D2( (b[0] + i*dd[0], b[1] + i*dd[1]) )

print("Part 1")
print(sum(1 for x in D1 if D1[x] > 1))

print("Part 2")
print(sum(1 for x in D2 if D2[x] > 1))