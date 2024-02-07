# https://adventofcode.com/2022/day/21

import sys

monkeys = {}

for line in sys.stdin:
    name, formula = line.split(':')
    monkeys[name] = formula.split()


def compute(name):
    formula = monkeys[name]
    if len(formula) == 1:
        return int(formula[0])
    left_val = compute(formula[0])
    right_val = compute(formula[2])
    match formula[1]:
        case '+':
            return left_val + right_val
        case '-':
            return left_val - right_val
        case '*':
            return left_val * right_val
        case '/':
            return left_val / right_val


print(int(compute('root')))
