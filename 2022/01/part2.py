# https://adventofcode.com/2022/day/1

import sys

import more_itertools

chunks = more_itertools.split_at(sys.stdin, lambda line: line == '\n')
sorted_ = sorted(sum(int(i) for i in chunk) for chunk in chunks)
print(sorted_[-1] + sorted_[-2] + sorted_[-3])
