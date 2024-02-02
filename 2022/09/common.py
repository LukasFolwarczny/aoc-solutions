import sys

from lib import Vec2D


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def solve(length):
    instructions = []

    for line in sys.stdin:
        direction, steps_str = line.strip().split()
        instructions.append((direction, int(steps_str)))

    positions = [Vec2D(0, 0) for _ in range(length)]
    visited = {(0, 0)}

    for instruction in instructions:
        delta = Vec2D(0, 0)
        match instruction[0]:
            case 'U':
                delta.x = 1
            case 'D':
                delta.x = -1
            case 'R':
                delta.y = 1
            case 'L':
                delta.y = -1
        for _ in range(instruction[1]):
            positions[0] += delta
            for knot in range(1, length):
                delta_consecutive = positions[knot - 1] - positions[knot]
                if abs(delta_consecutive.x) > 1 and delta_consecutive.y == 0:
                    positions[knot].x += delta_consecutive.x // 2
                elif abs(delta_consecutive.y) > 1 and delta_consecutive.x == 0:
                    positions[knot].y += delta_consecutive.y // 2
                elif (
                    abs(delta_consecutive.x) > 1
                    and abs(delta_consecutive.y) > 0
                ) or (
                    abs(delta_consecutive.x) > 0
                    and abs(delta_consecutive.y) > 1
                ):
                    positions[knot] += (
                        sgn(delta_consecutive.x),
                        sgn(delta_consecutive.y),
                    )
            visited.add(tuple(positions[-1]))

    return len(visited)
