# https://adventofcode.com/2021/day/10

import sys

score = { ')': 3, ']': 57, '}' : 1197, '>': 25137 }
score2 = { ')': 1, ']': 2, '}' : 3, '>': 4 }
matching = { '(': ')', '[': ']', '{' : '}', '<': '>'}
invm = {}

for m in matching:
    invm[matching[m]] = m

result = 0

scores = []

for line in sys.stdin:
    myscore = 0
    line = line.strip()
    depth = { '(': 0, '[': 0, '{' : 0, '<': 0}
    stack = []
    broken = False
    for c in line:
        if c in matching:
            stack.append(c)
            depth[c] += 1
        elif c in invm:
            d = invm[c]
            e = stack.pop()
            if e != d:
                result += score[c]
                broken = True
                break
    if not broken:
        for x in reversed(stack):
            myscore *= 5
            myscore += score2[matching[x]]
        scores.append(myscore)
            

print("Part 1")
print(result)

scores.sort()
print("Part 2")
print(scores[len(scores) // 2])


