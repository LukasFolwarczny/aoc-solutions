# https://adventofcode.com/2022/day/20

import sys

A = [int(line) for line in sys.stdin]
N = len(A)

D = list(range(N))  # D[i] determines the position of A[i]
E = list(range(N))  # E[k] = i means that D[i] = k

for i in range(N):
    pos = D[i]
    value = A[i] % (N - 1)
    for t in range(1, value + 1):
        id = E[(pos + t) % N]
        D[id] = (D[id] - 1) % N
        E[D[id]] = id
    D[i] = (pos + value) % N
    E[D[i]] = i

pos_zero = 0

for i in range(N):
    if A[E[i]] == 0:
        pos_zero = i

result = sum(A[E[(pos_zero + shift) % N]] for shift in (1000, 2000, 3000))
print(result)
