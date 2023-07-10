# https://adventofcode.com/2022/day/9
import sys

# It would make more sense to implement it with a set of coordinates instead of a two-dimensional list.

inst = []

for l in sys.stdin:
    d = l.strip().split(' ')[0]
    x = int(l.strip().split(' ')[1])
    inst.append((d,x))

maxr = maxs = 0
minr = mins = 0

r = s = 0

for i in inst:
    match i[0]:
        case 'U':
            r += i[1]
            maxr=max(r,maxr)
        case 'D':
            r -= i[1]
            minr=min(r,minr)
        case 'L':
            s -= i[1]
            mins=min(s,mins)
        case 'R':
            s += i[1]
            maxs=max(s,maxs)

#print(maxr,minr,maxs,mins)

R = maxr - minr + 1
S = maxs - mins + 1

def solve(L):
    V = [[False] * S for _ in range(R)]

    #print("Bounds", R, S)

    r = [-minr] * L
    s = [-mins] * L
    V[r[L-1]][s[L-1]] = True

    for i in inst:
        dr = ds = 0
        if i[0] == 'U':
            dr = 1
        if i[0] == 'D':
            dr = -1
        if i[0] == 'L':
            ds = -1
        if i[0] == 'R':
            ds = 1
        for k in range(i[1]):
            r[0] += dr
            s[0] += ds
            for bod in range(1,L):
                dir = r[bod-1] - r[bod]
                dis = s[bod-1] - s[bod]
                if abs(dir) > 1 and abs(dis) == 0:
                    r[bod] += dir // 2
                elif abs(dis) > 1 and abs(dir) == 0:
                    s[bod] += dis // 2
                elif (abs(dir) > 1 and abs(dis) > 0) or (abs(dir) > 0 and abs(dis) > 1):
                    s[bod] += dis//abs(dis)
                    r[bod] += dir//abs(dir)
            V[r[L-1]][s[L-1]] = True

            '''
            print(rT,sT)
            for rx in range(len(V)):
                for sx in range(len(V[rx])):
                    if V[len(V)-1-rx][sx]: print("#",end='')
                    else:print(".",end='')
                print()
            '''

    return sum([1 for i in range(R) for j in range(S) if V[i][j]])

print("Part 1")
print(solve(2))
print("Part 2")
print(solve(10))