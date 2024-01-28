# https://adventofcode.com/2022/day/2

import sys

score = 0

for line in sys.stdin:
    a, b = line.split()
    player_1 = ord(a) - ord('A')
    player_2 = ord(b) - ord('X')

    score += 1 + player_2
    if player_1 == player_2:
        score += 3
    elif (player_1 + 1) % 3 == player_2:
        score += 6

print(score)
