# https://adventofcode.com/2022/day/14

import sys

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

S = []
M = set()

for l in sys.stdin:
    pairs = l.split("->")
    S.append([ (int(x.split(",")[0]),int(x.split(",")[1])) for x in pairs ])


maxy = -2**32
for j in S:
    maxy = max(max(i[1] for i in j),maxy)

for line in S:
    p = line[0]
    for i in range(1,len(line)):
        d = (sign(line[i][0] - p[0]), sign(line[i][1] - p[1]))
        while p != line[i]:
            M.add(p)
            pp = (p[0] + d[0],p[1]+d[1])
            p = pp
        M.add(p)


bound = maxy+2
part1 = True
#print(sorted(list(M)))

def fall():
    px,py = 500,0
    if (px,py) in M:
        return False
    while py < bound-1:
        if (px,py+1) in M:
            if (px-1,py+1) not in M:
                px -= 1
                py += 1
            elif (px+1,py+1) not in M:
                px += 1
                py += 1
            else:
                M.add((px,py))
                return True
        else:
            py += 1
    if part1:
        return False
    else:
        M.add((px,py))
        return True

M2 = M.copy()

fallen = 0
while fall():
    fallen += 1
print("Part 1")
print(fallen)

M = M2
part1 = False
bound = maxy+2
fallen = 0
while fall():
    fallen += 1
print("Part 2")
print(fallen)