# https://adventofcode.com/2022/day/13

import sys
import functools

debug = False

s = 0

def parseline(l):
    stack = []
    current = []
    numstr = ''
    for c in l:
        if c == '[':
            stack.append(current)
            current = []
        elif c == ']':
            if numstr != '':
                current.append(int(numstr))
            numstr = ''
            parent = stack.pop()
            parent.append(current)
            current = parent
        elif c == ',':
            if numstr != '':
                current.append(int(numstr))
            numstr = ''
        else:
            numstr += c
    return current

def compare(s1,s2):
    if isinstance(s1,int) and isinstance(s2,int):
        if s1 < s2:
           return 1
        if s1 == s2:
            return 0
        if s2 < s1:
            return -1
    if isinstance(s1,int):
        return compare([s1],s2)
    if isinstance(s2,int):
        return compare(s1,[s2])
    
    i1 = i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        e1 = s1[i1]
        e2 = s2[i2]
        comp = compare(e1,e2)
        if comp == -1:
            return -1
        if comp == 1:
            return 1
        i1 += 1
        i2 += 1
    if len(s1) == len(s2):
        return 0
    if len(s1) > len(s2):
        return -1
    return 1

i = 1

L = [[[2]],[[6]]]

while l1 := sys.stdin.readline():
    l2 = sys.stdin.readline()
    sys.stdin.readline()
    s1 = parseline(l1)
    s2 = parseline(l2)
    if debug:
        print('i = ', i)
        print(s1)
        print(s2)
    if compare(s1,s2) == 1:
        if debug:
            print('true')
        s += i
    i += 1
    L.append(s1)
    L.append(s2)
        

print('Part 1')
print(s)

L.sort(key=functools.cmp_to_key(compare),reverse=True)
i1 = L.index([[2]]) + 1
i2 = L.index([[6]]) + 1
print('Part 2')
print(i1*i2)