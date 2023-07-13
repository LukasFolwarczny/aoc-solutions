# https://adventofcode.com/2022/day/22

import sys

M = []
instr = []
D = ((0, 1), (1, 0), (0, -1), (-1, 0))

while (line := sys.stdin.readline()) != "\n":
    M.append(line[:-1])

instrline = sys.stdin.readline()

x = 0

for c in instrline.strip():
    if c in ('L', 'R'):
        if x != 0:
            instr.append(x)
            x = 0
        instr.append(c)
    else:
        x = x*10 + ord(c) - ord('0')
if x != 0:
    instr.append(x)

R = len(M)
S = max([len(row) for row in M])
maxs = []
mins = []
maxr = []
minr = []

for r in range(R):
    minsakt = 0
    while M[r][minsakt] == ' ':
        minsakt += 1
    mins.append(minsakt)
    maxs.append(len(M[r]) - 1)

for s in range(S):
    minrakt = 0
    if s <= len(M[0])-1:
        while M[minrakt][s] == ' ':
            minrakt += 1
    else:
        while len(M[minrakt])-1 < s:
            minrakt += 1
    minr.append(minrakt)
    maxrakt = R-1
    if s <= len(M[R-1]) - 1:
        while M[maxrakt][s] == ' ':
            maxrakt -= 1
    else:
        while len(M[maxrakt])-1 < s:
            maxrakt -= 1
    maxr.append(maxrakt)

pos = (0,mins[0])
dir = 0

for instrukce in instr:
    if instrukce == 'L':
        dir = (dir - 1) % 4
    elif instrukce == 'R':
        dir = (dir + 1) % 4
    else:
        for step in range(instrukce):
            (dr,ds) = D[dir]
            (r,s) = pos
            if dr == 0:
                if mins[r] <= s+ds <= maxs[r]:
                    if M[r][s+ds] == '.':
                        pos = (r,s+ds)
                    else:
                        break
                else:
                    if ds == 1:
                        if M[r][mins[r]] == '.':
                            pos = (r, mins[r])
                        else:
                            break
                    if ds == -1:
                        if M[r][maxs[r]] == '.':
                            pos = (r, maxs[r])
                        else:
                            break
            if ds == 0:
                if minr[s] <= r+dr <= maxr[s]:
                    if M[r+dr][s] == '.':
                        pos = (r+dr,s)
                    else:
                        break
                else:
                    if dr == 1:
                        if M[minr[s]][s] == '.':
                            pos = (minr[s], s)
                        else:
                            break
                    if dr == -1:
                        if M[maxr[s]][s] == '.':
                            pos = (maxr[s], s)
                        else:
                            break

print("Part 1")
print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + dir)