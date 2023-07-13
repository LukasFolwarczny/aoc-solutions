# https://adventofcode.com/2022/day/20

import sys

N = 0
Aorig = []

debug = False

for l in sys.stdin:
    v = int(l)
    Aorig.append(v*811589153)

N = len(Aorig)

A = [ x % (N-1) for x in Aorig ]


D = list(range(N))
E = D.copy()

for iter in range(10):
    if debug:
        for i in range(N):
            print(Aorig[E[i]], end=", ")
        print()
    for i in range(N):
        if debug:
            for j in range(N):
                print(A[E[j]], end=", ")
            print()
        pos = D[i]
        v = A[i]
        for t in range(1,v+1):
            id = E[(pos+t) % N]
            D[id] = (D[id] + N - 1) % N
            E[D[id]] = id
        D[i] = (pos + v) % N
        E[D[i]] = i
    

pos_zero = 0

for i in range(N):
    if Aorig[E[i]] == 0:
        pos_zero = i

R = [ Aorig[E[(pos_zero + shift) % N]] for shift in (1000,2000,3000) ]

print("Nums:", R)
print("Part 2")
print(sum(R))
