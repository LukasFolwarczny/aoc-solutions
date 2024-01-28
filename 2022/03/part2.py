# https://adventofcode.com/2022/day/3

import sys
from functools import reduce
from itertools import batched
from operator import and_

priority_sum = 0

for triple in batched(sys.stdin, 3):
    intersection = reduce(and_, (set(x.strip()) for x in triple))
    x = ord(intersection.pop())
    if x < ord('a'):
        priority_sum += x - ord('A') + 27
    else:
        priority_sum += x - ord('a') + 1

print(priority_sum)
