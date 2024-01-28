# https://adventofcode.com/2022/day/7

import sys


class Node:
    def __init__(self, parent):
        self.parent = parent
        if parent is not None:
            parent.children.append(self)
        self.children = []
        self.files = 0
        self.sum = 0


root = Node(None)
curr = root

for line in sys.stdin:
    if ord('0') <= ord(line[0]) <= ord('9'):
        curr.files += int(line.split(' ')[0])
    elif line[0] == '$':
        if line[2] == 'l':
            pass
        elif line[2] == 'c':  # cd
            if line[5] == '.':
                curr = curr.parent
            elif line[5] == '/':
                pass  # root
            else:  # cd some_dir
                curr = Node(curr)


def compute_sum(node):
    node.sum = node.files
    for c in node.children:
        compute_sum(c)
        node.sum += c.sum


def find_folder_min(size_bound, node):
    min_ = 2**32
    if node.sum >= size_bound:
        min_ = node.sum
    min_ = min(
        [min_] + [find_folder_min(size_bound, c) for c in node.children]
    )
    return min_


compute_sum(root)
result = find_folder_min(root.sum - 40_000_000, root)

print(result)
