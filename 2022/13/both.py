# https://adventofcode.com/2022/day/13

import sys
from functools import cmp_to_key

from more_itertools import split_at


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left == right:
            return 0
        if right < left:
            return -1
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])

    for a, b in zip(left, right):
        comp = compare(a, b)
        if comp != 0:
            return comp
        if comp == 1:
            return 1
    return compare(len(left), len(right))


L = [[[2]], [[6]]]

sum_ = 0

for i, (line_1, line_2) in enumerate(
    split_at(sys.stdin, lambda line: line.isspace())
):
    seq_1 = eval(line_1)
    seq_2 = eval(line_2)
    if compare(seq_1, seq_2) == 1:
        sum_ += i + 1
    L.append(seq_1)
    L.append(seq_2)


print('Part 1')
print(sum_)

L.sort(key=cmp_to_key(compare), reverse=True)
i1 = L.index([[2]]) + 1
i2 = L.index([[6]]) + 1

print('Part 2')
print(i1 * i2)
