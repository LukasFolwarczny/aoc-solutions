# https://adventofcode.com/2022/day/16

import sys
from collections import namedtuple

TOTAL_TIME = 30

Valve = namedtuple('Valve', ['id', 'pos_id', 'flow', 'label', 'leads_to'])
State = namedtuple('State', ['valve', 'time', 'open'])

M = 0  # number of valves with positive flow
label_to_id = {}
pre_valves = []

for i, line in enumerate(sys.stdin):
    splitted = line.strip().split()
    label = splitted[1]
    label_to_id[label] = i
    flow = int(splitted[4].split('=')[1].split(';')[0])
    if flow > 0:
        pos_id = M
        M += 1
    else:
        pos_id = -1
    leads_to = []
    for label_to in splitted[9:]:
        leads_to.append(label_to[:2])
    pre_valves.append((i, pos_id, flow, label, leads_to))

valves = []
for id, pos_id, flow, label, leads_to in pre_valves:
    leads_to_ids = [label_to_id[label] for label in leads_to]
    valves.append(Valve(id, pos_id, flow, label, leads_to_ids))

cache = {}


def solve(state):
    if state.time == 0:
        return 0
    if state in cache:
        return cache[state]
    current = valves[state.valve]
    optimal = 0
    if current.flow > 0 and state.open & 2**current.pos_id == 0:
        new_state = State(
            state.valve, state.time - 1, state.open | 2**current.pos_id
        )
        optimal = solve(new_state) + (state.time - 1) * current.flow
    for next in current.leads_to:
        optimal = max(optimal, solve(State(next, state.time - 1, state.open)))
    cache[state] = optimal
    return optimal


initial = State(label_to_id['AA'], TOTAL_TIME, 0)
print(solve(initial))
