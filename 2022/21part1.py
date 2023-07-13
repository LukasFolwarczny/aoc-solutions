# https://adventofcode.com/2022/day/21

import sys

D = {}

def compute(id):
    ll = D[id].split()
    if len(ll) == 1:
        return int(ll[0])
    match ll[1]:
        case "+":
            return compute(ll[0]) + compute(ll[2])
        case "-":
            return compute(ll[0]) - compute(ll[2])
        case "*":
            return compute(ll[0]) * compute(ll[2])
        case "/":
            return compute(ll[0]) // compute(ll[2])

for  l in sys.stdin:
    lx = l.split(':')
    D[lx[0]] = lx[1]

print(compute("root"))