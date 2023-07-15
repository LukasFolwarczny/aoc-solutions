# https://adventofcode.com/2021/day/6

import sys

inp = sys.stdin.readline()

initial = [ int(x) for x in inp.split(',') ]

state = [ 0 ] * 9

for v in initial:
    state[v] += 1

for d in range(256):
    state1 = [ 0 ] * 9
    for c in range(1,9):
        state1[c-1] = state[c]
    state1[8] = state[0]
    state1[6] += state[0]
    state = state1
    if d == 79:
        print("Part 1")
        print(sum(state))

print("Part 2")
print(sum(state))