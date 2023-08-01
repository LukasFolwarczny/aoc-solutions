# https://adventofcode.com/2020/day/7

import sys
from collections import namedtuple

D = {}

for line in sys.stdin:
    color = line.split(" bags")[0]
    contains = line.split("contain ")[1]
    L = []
    if contains.split()[0] != "no":
        for x in contains.split(','):
            n = int(x.split()[0])
            c = x.split()[1] + ' ' + x.split()[2]
            L.append((n,c))
    D[color] = L

V = set()
Dyn = {}

def dfs(color):
    if color in Dyn.keys():
        return Dyn[color]
    if color == "shiny gold":
        return True
    Dyn[color] = any( dfs(x[1]) for x in D[color])
    return Dyn[color]

def scount(color):
    return 1 + sum( x[0] * scount(x[1]) for x in D[color])

count = 0

for x in D.keys():
    if dfs(x):
        count += 1

print("Part 1")
print(count - 1)

print("Part 2")
print(scount("shiny gold") - 1)