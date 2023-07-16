# https://adventofcode.com/2022/day/17

import sys

instructions = sys.stdin.readline().strip()
iterations = 2022

S = [ [ (0,0), (0, 1), (0, 2), (0, 3)], [(1,0), (0, 1), (1,1), (2,1), (1,2)], [(0,0), (0,1), (0,2), (1,2),(2,2)], [ (0,0), (1,0), (2,0), (3,0)], [(0,0), (1,0), (0,1),(1,1)] ]
F = set() # fallen

top = -1
p = 0

debug = False

def is_down(s, pos):
    for x in s:
        if x[0]+pos[0] == 0 or (x[0]+pos[0]-1, x[1]+pos[1]) in F:
            return True
    return False

def move_left(s, pos):
    for x in s:
        if x[1]+pos[1] == 0 or (x[0]+pos[0], x[1]+pos[1]-1) in F:
            return pos
    return (pos[0],pos[1]-1)

def move_right(s, pos):
    for x in s:
        if x[1]+pos[1] == 6 or (x[0]+pos[0], x[1]+pos[1]+1) in F:
            return pos
    return (pos[0],pos[1]+1)


def visualize_top20():
    for i in range(top+1,top-20,-1):
        l = ""
        for j in range(7):
            if (i,j) in F:
                l += "#"
            else:
                l += "."
        print(l)


for i in range(iterations):
    s = S[i%5]
    pos = (top+4,2)
    while True:
        instr = instructions[p % len(instructions)]
        p += 1
        if instr == "<":
            pos = move_left(s,pos)
        else:
            pos = move_right(s,pos)
        if is_down(s, pos):
            break
        else:
            pos = (pos[0]-1, pos[1])
    for x in s:
        F.add((pos[0]+x[0],pos[1]+x[1]))
        top = max(top, pos[0]+x[0])
    if debug:
        print("i = ", i)
        visualize_top20()
        print("p = ", p)
        print("top = ", top)


print("Part 1")
print(top+1)