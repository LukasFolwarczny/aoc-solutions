# https://adventofcode.com/2022/day/1

import sys

import more_itertools

chunks = more_itertools.split_at(sys.stdin, lambda line: line.isspace())
result = max(sum(int(i) for i in chunk) for chunk in chunks)
print(result)
