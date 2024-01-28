# https://adventofcode.com/2022/day/5

import sys

S = tuple([[] for _ in range(9)])

for line in sys.stdin:
    if line == '\n':
        continue
    elif line[1] == 'o':
        L = line.split(' ')
        count = int(L[1])
        from_ = int(L[3]) - 1
        to = int(L[5]) - 1
        T = []
        for _ in range(count):
            T.append(S[from_].pop())
        for x in reversed(T):
            S[to].append(x)
    elif line[1] == '1':
        for i in range(9):
            S[i].reverse()
    else:
        for i in range(9):
            ind = 1 + i * 4
            if ind < len(line) and line[ind] != ' ':
                S[i].append(line[ind])

top_crates = ''.join(S[i][-1] for i in range(9) if len(S[i]))

print(top_crates)
