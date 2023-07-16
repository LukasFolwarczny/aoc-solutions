# https://adventofcode.com/2021/day/14

import sys

start = sys.stdin.readline().strip()
sys.stdin.readline()

D = {}
MM = {}

total_steps = 40

def compute_pair(c1, c2, steps):
    if (c1,c2,steps) in MM:
        return MM[(c1,c2,steps)]
    R = [0] * 26 
    if steps == 0 or (c1,c2) not in D:
        R[c1] = 0
        R[c2] = 1
        return R
    R = compute_pair(c1, D[(c1,c2)], steps-1)
    R2 = compute_pair(D[(c1,c2)], c2, steps-1)
    MM[(c1,c2,steps)] = [ R[i] + R2[i] for i in range(26) ]
    return MM[(c1,c2,steps)]
    
result = [0] * 26

for line in sys.stdin:
    ll = line.strip().split(" -> ")
    D[(ord(ll[0][0])-ord('A'),ord(ll[0][1])-ord('A'))] = ord(ll[1])-ord('A')

for i in range(len(start)-1):
    R = compute_pair(ord(start[i])-ord('A'),ord(start[i+1])-ord('A'), total_steps)
    for j in range(26):
        result[j] += R[j]
result[ord(start[0]) - ord('A')] += 1

minc = min(i for i in result if i > 0)
maxc = max(result)
print("Part 2")
print(maxc - minc)