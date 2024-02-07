# https://adventofcode.com/2022/day/21

import sys

monkeys = {}

for line in sys.stdin:
    name, formula = line.split(':')
    monkeys[name] = formula.split()

determined = set()


def is_determined(name):
    if name == 'humn':
        return False
    if len(monkeys[name]) == 1:
        determined.add(name)
        return True
    left = monkeys[name][0]
    right = monkeys[name][2]
    left_determined = is_determined(left)
    right_determined = is_determined(right)
    if left_determined and right_determined:
        determined.add(name)
        return True
    return False


is_determined('root')


def compute(name):
    formula = monkeys[name]
    if len(formula) == 1:
        return int(formula[0])
    left, op, right = formula
    match op:
        case '+':
            return compute(left) + compute(right)
        case '-':
            return compute(left) - compute(right)
        case '*':
            return compute(left) * compute(right)
        case '/':
            return compute(left) / compute(right)


def solve(name, desired):
    if name == 'humn':
        return desired
    left, op, right = monkeys[name]
    if left in determined:
        left_val = compute(left)
        match op:
            case '+':
                return solve(right, desired - left_val)
            case '-':
                return solve(right, left_val - desired)
            case '*':
                return solve(right, desired / left_val)
            case '/':
                return solve(right, left_val / desired)
    right_val = compute(right)
    match op:
        case '+':
            return solve(left, desired - right_val)
        case '-':
            return solve(left, desired + right_val)
        case '*':
            return solve(left, desired / right_val)
        case '/':
            return solve(left, desired * right_val)


left, _, right = monkeys['root']
if left in determined:
    print(int(solve(right, compute(left))))
else:
    print(int(solve(left, compute(right))))
