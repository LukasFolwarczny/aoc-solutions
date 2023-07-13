# https://adventofcode.com/2022/day/24

import sys
import collections

blizz = []
V = set()

R = 0
S = 0

for line in sys.stdin:
    S = len(line.strip())
    for s, c in enumerate(line.strip()):
        if c in ('<','>','^','v'):
            blizz.append((R,s,c))
    R += 1

Q = collections.deque()
Q.append((0,1,0,0))
V.add((0,1,0,0))

part1solved = False
B = set()

current_t = 0

def is_free(r, s, t):
    global current_t
    if current_t != t:
        blizz_pos(t)
        current_t = t
        if t % 20 == 0:
            print("xxx ", current_t)
    if (r,s) in B:
        return False
    return True

def blizz_pos(t):
    B.clear()
    for b in blizz:
        match b[2]:
            case '<':
                B.add((b[0], (b[1] - 1 - t) % (S-2) + 1))
            case '>':
                B.add((b[0], (t + b[1] - 1) % (S-2) + 1))
            case '^':
                B.add(((b[0] - 1 - t) % (R-2) + 1, b[1]))
            case 'v':
                B.add(((t + b[0] - 1) % (R-2) + 1, b[1]))


while len(Q):
    (r,s,t,state) = Q.popleft()
    if r == R-1 and s == S-2 and state == 2:
        print("Part 2")
        print(t)
        break
    if r == R-1 and s == S-2 and state == 0 and not part1solved:
        print("Part 1")
        print(t)
        part1solved = True
    for dd in ((1,0),(-1,0),(0,1),(0,-1),(0,0)):
        new_r = r + dd[0]
        new_s = s + dd[1]
        if (1 <= new_r < R-1 or (new_r == 0 and new_s == 1) or (new_r == R-1 and new_s == S-2)) and (1 <= new_s < S-1):
            newstate = state
            if state == 0 and new_r == R-1 and new_s == S-2:
                state = 1
            elif state == 1 and new_r == 0 and new_s == 1:
                state = 2
            if is_free(new_r,new_s,t+1) and not (new_r,new_s,t+1,newstate) in V:
                V.add((new_r,new_s,t+1,newstate))
                Q.append((new_r,new_s,t+1,newstate))