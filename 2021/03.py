# https://adventofcode.com/2021/day/3

import sys

lines = [ l.strip() for l in sys.stdin ]
total = len(lines)
N = len(lines[0])
vals = [ sum(int(lines[i][n]) for i in range(total)) for n in range(N) ]

gamma = 0
epsilon = 0

for v in vals:
    gamma *= 2
    epsilon *= 2
    if v >= total/2:
        gamma += 1
    else:
        epsilon += 1

print("Part 1")
print(gamma*epsilon)

def column_sum(L, i):
    return sum(int(L[j][i]) for j in range(len(L)))

mylist = lines
pos = 0
while len(mylist) > 1:
    bit = '0'
    if column_sum(mylist, pos) >= len(mylist)/2:
        bit = '1'
    mylist = [ x for x in mylist if x[pos] == bit ]
    pos += 1

oxygen = int(mylist[0],2)

mylist = lines
pos = 0
while len(mylist) > 1:
    bit = '1'
    if column_sum(mylist, pos) >= len(mylist)/2:
        bit = '0'
    mylist = [ x for x in mylist if x[pos] == bit ]
    pos += 1


co = int(mylist[0],2)

print("Part 2")
print(oxygen*co)