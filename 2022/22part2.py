# https://adventofcode.com/2022/day/22

# Unfortunately, this only works for my particular input.

import sys

M = []
instr = []
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while (line := sys.stdin.readline()) != "\n":
    M.append(line[:-1])

instrline = sys.stdin.readline()

x = 0

def compute_face(r,s):
    if r < 50:
        if 50 <= s < 100:
            return 0
        if 100 <= s < 150:
            return 1
    if 50 <= r < 100:
        return 2
    if 100 <= r < 150:
        if 0 <= s < 50:
            return 3
        if 50 <= s < 100:
            return 4
    if 150 <= r < 200:
        return 5
    print("WRONG ", r, s)

def jump(r, s, dir):
    face = compute_face(r,s)
    newdir = -1
    newpos = (-1,-1)
    if dir == 0:
        if face == 1:
            newdir = 2
            newpos = (49-r+100 ,s-50)
        if face == 2:
            newdir = 3
            newpos = (49, r)
        if face == 4:
            newdir = 2
            newpos = (49 - (r-100), 149)
        if face == 5:
            newdir = 3
            newpos = (149, r-100)
    if dir == 1:
        if face == 1:
            newdir = 2
            newpos = (s-50 ,99)
        if face == 4:
            newdir = 2
            newpos = (s+100, 49)
        if face == 5:
            newdir = 1
            newpos = (0, s+100)
    if dir == 2:
        if face == 0:
            newdir = 0
            newpos = (149-r, 0)
        if face == 2:
            newdir = 1
            newpos = (100, r)
        if face == 3:
            newdir = 0
            newpos = (50, 149 - r)
        if face == 5:
            newdir = 1
            newpos = (0, r - 100)
    if dir == 3:
        if face == 0:
            newdir = 0
            newpos = (s + 100, 0)
        if face == 1:
            newdir = 3
            newpos = (199, s-100)
        if face == 3:
            newdir = 0
            newpos = (s+50, 50)
    if newpos[0] < 0 or newpos[1] < 0 or newdir == -1:
        print(face, "ERROR")
    return newpos,newdir


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
                    newpos,newdir = jump(r, s, dir)
                    if M[newpos[0]][newpos[1]] == '.':
                        pos = newpos
                        dir = newdir
                    else:
                        break
            if ds == 0:
                if minr[s] <= r+dr <= maxr[s]:
                    if M[r+dr][s] == '.':
                        pos = (r+dr,s)
                    else:
                        break
                else:
                    newpos,newdir = jump(r, s, dir)
                    if M[newpos[0]][newpos[1]] == '.':
                        pos = newpos
                        dir = newdir
                    else:
                        break

print("Part 2")
print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + dir)