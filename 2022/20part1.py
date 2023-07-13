# https://adventofcode.com/2022/day/20

import sys

N = 0
A = []

debug = False

for l in sys.stdin:
    v = int(l)
    A.append(v)

N = len(A)

D = list(range(N))
E = D.copy()

for i in range(N):
    if debug:
        for j in range(N):
            print(A[E[j]], end=", ")
        print()
    pos = D[i]
    v = A[i]
    if v > 0:
        for t in range(1,v+1):
            id = E[(pos+t) % N]
            D[id] = (D[id] - 1) % N
            E[D[id]] = id
        D[i] = (pos + v) % N
        E[D[i]] = i
    if v < 0:
        for t in range(1,1-v):
            id = E[(pos-t) % N]
            D[id] = (D[id] + 1) % N
            E[D[id]] = id
        D[i] = (pos + v) % N
        E[D[i]] = i

pos_zero = 0

for i in range(N):
    if A[E[i]] == 0:
        pos_zero = i

R = [ A[E[(pos_zero + shift) % N]] for shift in (1000,2000,3000) ]

print("Nums:", R)
print("Part 1")
print(sum(R))