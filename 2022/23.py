# https://adventofcode.com/2022/day/23

import sys

S = set()

directions = [ 'N', 'S', 'W', 'E']
D = { 'N': (-1,0), 'S' : (1,0), 'E' : (0,1), 'W' : (0,-1)}
D2 = { 'N': [(-1,0),(-1,1),(-1,-1)], 'S' : [(1,0),(1,-1),(1,1)], 'E' : [(0,1),(1,1),(-1,1)], 'W' : [(0,-1),(1,-1),(-1,-1)]}

rounds = 10

r = 0
for line in sys.stdin:
    for s in range(len(line.strip())):
        if line[s] == '#':
            S.add((r,s))
    r += 1

for r in range(2**32):
    proposals = set()
    badcoords = set()
    actions = {}
    for p in S:
        good = False
        for dr in [0,1,-1]:
            for ds in [0,1,-1]:
                if (dr != 0 or ds != 0) and (p[0]+dr,p[1]+ds) in S:
                    good = True
        if not good:
            actions[p] = p
        else:
            moved = False
            for d in directions:
                canmove = True
                for dd in D2[d]:
                    if (p[0]+dd[0],p[1]+dd[1]) in S:
                        canmove = False
                if canmove:
                    actions[p] = (p[0]+D[d][0],p[1]+D[d][1])
                    if actions[p] in proposals:
                        badcoords.add(actions[p])
                    proposals.add(actions[p])
                    moved = True
                    break
            if not moved:
                actions[p] = p
    for p in S:
        if actions[p] in badcoords:
            actions[p] = p
    '''
    for r in range(-20,20):
        for s in range(-20,20):
            if (r,s) in S:
                print("#", end="")
            else:
                print(".",end="")
        print()
    '''
    d = directions.pop(0)
    directions.append(d)
    finished = True
    for p in S:
        if actions[p] != p:
            finished = False
    if finished:
        print("Part 2")
        print(r + 1)
        exit()
    S = set(actions.values())
    if r == 9:
        maxr = -2**32
        maxs = -2**32
        minr = 2**32
        mins = 2**32
        for x in S:
            maxr = max(maxr,x[0])
            maxs = max(maxs,x[1])
            minr = min(minr,x[0])
            mins = min(mins,x[1])
        print("Part 1")
        print((maxr-minr+1)*(maxs-mins+1)-len(S))
    

