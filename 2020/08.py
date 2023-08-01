# https://adventofcode.com/2020/day/8

import sys

I = []

for line in sys.stdin:
    s,t = line.strip().split()
    I.append((s,int(t)))

def simulate(instructions):
    instr = 0
    acc = 0
    S = set()

    while instr < len(instructions) and instr not in S:
        S.add(instr)
        if instructions[instr][0] == "jmp":
            instr += instructions[instr][1]
        elif instructions[instr][0] == "acc":
            acc += instructions[instr][1]
            instr += 1
        else:
            instr += 1
    return instr, acc

print("Part 1")
print(simulate(I)[1])

for i in range(len(I)):
    if I[i][0] == "nop":
        J = I.copy()
        J[i] = ("jmp", I[i][1])
    elif I[i][0] == "jmp":
        J = I.copy()
        J[i] = ("nop", I[i][1])
    else:
        continue
    instr, acc = simulate(J)
    if instr == len(J):
        print("Part 2")
        print(acc)
