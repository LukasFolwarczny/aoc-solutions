# https://adventofcode.com/2021/day/4

import sys

D = 5

def board_score(board, chosen):
    won = any( all( board[row][col] in chosen for row in range(D)) for col in range(5) ) or \
        any( all( board[row][col] in chosen for col in range(D)) for row in range(5) )

    if not won:
        return -1
    return sum( board[row][col] for row in range(D) for col in range(D) if board[row][col] not in chosen) * chosen[-1]

lines = sys.stdin.readlines()

rands = [ int(i) for i in lines[0].split(',') ]
boards = []

i = 2

while i < len(lines):
    board = []
    for j in range(i, i+D):
        oneline = [ int(k) for k in lines[j].split() ]
        board.append(oneline)
    boards.append(board)
    i += D + 1


score = -1
part1solved = False
win = [ False for _ in range(len(boards)) ]

for n in range(len(rands)):
    cho = rands[0:n+1]

    for i, b in enumerate(boards):
        score = board_score(b, cho)
        if not part1solved and score > -1:
            print("Part 1")
            print(score)
            part1solved = True
        if not win[i] and score > -1:
            win[i] = True
        if sum(win) == len(boards):
            print("Part 2")
            print(score)
            exit()