# https://adventofcode.com/2020/day/5

import sys

L = [ line.strip() for line in sys.stdin ]
IDs = set()

for code in L:
    rowcode = code[:7]
    colcode = code[7:]
    row = 0
    for x in rowcode:
        if x == 'B':
            row = row * 2 + 1
        else:
            row = row * 2
    col = 0
    for y in colcode:
        if y == 'R':
            col = col * 2 + 1
        else:
            col = col * 2
    id = 8 * row + col
    IDs.add(id)

maxid = max(IDs)

print("Part 1")
print(maxid)

for i in IDs:
    if i+1 not in IDs and i+2 in IDs:
        print("Part 2")
        print(i+1)