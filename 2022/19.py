# https://adventofcode.com/2022/day/19

import sys
import mip
import math


R = 4 # number of robots

def solve(T, bp):
    m = mip.Model()
    buying = [ [ m.add_var(var_type='B') for r in range(R) ] for t in range(T+1) ]
    robot_counts = [ [ m.add_var(var_type='I', lb=0) for r in range(R) ] for t in range(T+1) ]
    resources_before = [ [ m.add_var(var_type='I', lb=0) for r in range(R) ] for t in range(T+1) ]
    resources_after = [ [ m.add_var(var_type='I', lb=0) for r in range(R) ] for t in range(T+1) ]

    for t in range(1,T+1):
        m += mip.xsum(buying[t][r] for r in range(R)) <= 1
    
    m += robot_counts[0][0] == 1
    for r in range(1,R):
         m += robot_counts[0][r] == 0
    for r in range(R):
         m += resources_after[0][r] == 0
    for r in range(R):
         for t in range(1,T+1):
             m += resources_before[t][r] == resources_after[t-1][r] - mip.xsum(buying[t][s] * bp[s][r] for s in range(R))
             m += resources_after[t][r] == resources_before[t][r] + robot_counts[t-1][r]
             m += robot_counts[t][r] == robot_counts[t-1][r] + buying[t][r]

    m.objective = mip.maximize(resources_after[T][3])
    m.optimize(max_seconds=300)
    return m.objective_value

results_part1 = []
results_part2 = []

for l in sys.stdin:
    ll = l.split()
    bpid = int(ll[1].split(':')[0])
    costs = []
    costs.append((int(ll[6]),0,0,0))
    costs.append((int(ll[12]),0,0,0))
    costs.append((int(ll[18]),int(ll[21]),0,0))
    costs.append((int(ll[27]),0,int(ll[30]),0))
    results_part1.append(bpid * solve(24, costs))
    if len(results_part2) < 3:
        results_part2.append(solve(32,costs))

print("Part 1")
print(round(sum(results_part1)))

print("Part 2")
print(round(math.prod(results_part2)))