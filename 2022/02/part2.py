# https://adventofcode.com/2022/day/2

import sys

score = 0

for line in sys.stdin:
    a, b = line.split()
    player_1 = ord(a) - ord('A')
    player_2 = ord(b) - ord('X')

    match player_2:
        case 0:
            score += (player_1 + 2) % 3 + 1
        case 1:
            score += 3 + player_1 + 1
        case 2:
            score += 6 + (player_1 + 1) % 3 + 1

print(score)
