# https://adventofcode.com/2021/day/13

import sys

S = set()
folds = []

for line in sys.stdin:
    if line.strip() == '':
        continue
    lx = ''
    if len(lx := line.strip().split(',')) == 2:
        S.add((int(lx[0]),int(lx[1])))
    else:
        lx = line.strip().split('=')
        folds.append((lx[0][-1], int(lx[1])))



for f in folds:
    for s in S.copy():
        if f[0] == 'x':
            if s[0] > f[1]:
                t = (2*f[1] - s[0], s[1])
                S.remove(s)
                S.add(t)
        else:
            if s[1] > f[1]:
                t = (s[0], 2*f[1] - s[1])
                S.remove(s)
                S.add(t)
    if f == folds[0]:
        print("Part 1")
        print(len(S))

print("Part 2")
for r in range(6):
    for s in range(39):
        print('#' if (s,r) in S else '.', end='')
    print()




