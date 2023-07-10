# https://adventofcode.com/2022/day/7

import sys
from anytree import Node

r = Node("/", files=0,sum=0)
curr = r

p1sum = 0

for l in sys.stdin:
    if ord('0') <= ord(l[0]) <= ord('9'):
        curr.files += int(l.split(' ')[0])
    elif l[0] == '$':
        if l[2] == 'l':
            s = 0
        elif l[2] == 'c': # cd
            if l[5] == '.':
                curr = curr.parent
            elif l[5] == '/':
                s = 0 # root
            else: # cd somedire
                curr = Node(parent=curr,files=0,sum=0,name=curr.name+"/"+l.split(' ')[1])
    elif l[0] == 'd':
        s = 0

def countsum(xnode):
    xnode.sum = xnode.files
    for c in xnode.children:
        countsum(c)
        xnode.sum += c.sum
    if xnode.sum <= 100_000:
        global p1sum
        p1sum += xnode.sum

countsum(r)

def findfold(sizebound, xnode):
    mymin = 2**32
    if xnode.sum >= sizebound:
        mymin = xnode.sum
    mymin = min( [mymin] + [ findfold(sizebound, c) for c in xnode.children ] )
    return mymin

print("Part 1")
print(p1sum)
print("Part 2")
print(findfold(r.sum - 40_000_000, r))