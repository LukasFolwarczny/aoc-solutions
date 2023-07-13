# https://adventofcode.com/2022/day/21

import sys

D = {}

for  l in sys.stdin:
    lx = l.split(':')
    D[lx[0]] = lx[1]


def compute(id,want):
    ll = D[id].split()
    if id =="humn":
        return (want,True)
    if len(ll) == 1:
        return (int(ll[0]),False)
    p0 = compute(ll[0],-2**32)
    p1 = compute(ll[2],-2**32)
    if not (p0[1] or p1[1]):
        match ll[1]:
            case "+":
                return (p0[0] + p1[0],False)
            case "-":
                return (p0[0] - p1[0],False)
            case "*":
                return (p0[0] * p1[0],False)
            case "/":
                return (p0[0] // p1[0],False)
    else:
        if p0[1]:
            if id == "root":
                return (compute(ll[0], p1[0])[0], True)
            if want == -2**32:
                return (-2**32,True)
            match ll[1]:
                case "+":
                    return (compute(ll[0], want - p1[0])[0], True)
                case "-":
                    return (compute(ll[0], want + p1[0])[0], True)
                case "*":
                    return (compute(ll[0], want / p1[0])[0], True)
                case "/":
                    return (compute(ll[0], want * p1[0])[0], True)
        else:
            if id == "root":
                return (compute(ll[2], p0[0])[0], True)
            if want == -2**32:
                return (-2**32, True)
            match ll[1]:
                case "+":
                    return (compute(ll[2], want - p0[0])[0], True)
                case "-":
                    return (compute(ll[2], -want + p0[0])[0], True)
                case "*":
                    return (compute(ll[2], want / p0[0])[0], True)
                case "/":
                    return (compute(ll[2], p0[0] / want)[0], True)


print(compute("root",-2**32)[0])

