# https://adventofcode.com/2022/day/5

import sys

S = tuple([ [] for _ in range(9)])
S2 = tuple([ [] for _ in range(9)])


for l in sys.stdin:
    if l == "\n": continue
    elif l[1] == 'o':
        L = l.split(' ')
        q = int(L[1])
        fr = int(L[3]) - 1
        to = int(L[5]) - 1
        print(q, fr, to)
        T = []
        T2 = []
        for i in range(q):
           T.append(S[fr].pop())
           T2.append(S2[fr].pop())
        for x in T:
           S[to].append(x)
        for x in reversed(T2):
           S2[to].append(x)
    elif l[1] == '1':
        for i in range(9):
            S[i].reverse()
            S2[i].reverse()
    else:
        for i in range(9):
           ind = 1 + i * 4
           if ind < len(l) and l[ind] != ' ':
               S[i].append(l[ind])
               S2[i].append(l[ind])

out = ""
out2 = ""

for i in range(9):
   if len(S[i]):
       out += S[i][-1]
   if len(S2[i]):
       out2 += S2[i][-1]

print("Part 1") 
print(out) 
print("Part 2") 
print(out2) 