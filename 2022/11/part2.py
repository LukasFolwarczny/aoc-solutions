# https://adventofcode.com/2022/day/11

import sys
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    id: int
    items: list
    fun: Callable
    divisor: int
    where: int
    inspected: int = 0


def parse_fun(operation):
    match operation.split()[3:]:
        case ['+', 'old']:
            return lambda a: a * 2
        case ['*', 'old']:
            return lambda a: a**2
        case ['+', second]:
            return lambda a: a + int(second)
        case ['*', second]:
            return lambda a: a * int(second)


modulus = 1
monkeys = []
line = ''

while line := sys.stdin.readline():
    id = int(line.split()[1].split(':')[0])
    items = []
    for item in sys.stdin.readline().split(':')[1].split(','):
        items.append(int(item))
    fun = parse_fun(sys.stdin.readline().split(':')[1])
    divisor = int(sys.stdin.readline().split(':')[1].split()[2])
    where = [0, 0]
    where[1] = int(sys.stdin.readline().split(':')[1].split()[3])
    where[0] = int(sys.stdin.readline().split(':')[1].split()[3])
    monkeys.append(Monkey(id, items, fun, divisor, where))
    modulus *= divisor
    sys.stdin.readline()

for _ in range(10_000):
    for m in monkeys:
        for item in m.items:
            m.inspected += 1
            new = m.fun(item) % modulus
            monkeys[m.where[new % m.divisor == 0]].items.append(new)
        m.items = []

insp = sorted(m.inspected for m in monkeys)

print(insp[-1] * insp[-2])
