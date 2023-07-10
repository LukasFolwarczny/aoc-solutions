# https://adventofcode.com/2022/day/10

import sys

s = 0

cycle = 0
X = 1

O = []

def increment(X, cycle, s):
    cycle += 1
    if cycle in range(20,221,40):
        s += cycle * X
    return (cycle, s)

def printsym():
    #print(cycle,X)
    if (cycle-1)%40 in (X-1,X,X+1):
        print('#',end='')
    else:
        print('.',end='')
    if cycle % 40 == 0:
        print()


print("Part 2")
for l in sys.stdin:
    if l[0] == "n":
        cycle,s = increment(X, cycle, s)
        printsym()
    else:
        cycle,s = increment(X, cycle, s)
        printsym()
        cycle,s = increment(X, cycle, s)
        printsym()
        X += int(l.split(' ')[1])

print("Part 1")
print(s)