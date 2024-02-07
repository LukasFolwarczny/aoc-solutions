# aoc-solutions
My python solutions to the [Advent of Code](https://adventofcode.com) contest

## Purpose

If you are curious about my solutions, you can have a look.
I don't claim anything particular about the quality of the solutions. 🙂

## Usage

I use [python poetry](https://python-poetry.org/) for dependency management.

To install the dependencies, run:
```
poetry install
```

The solutions use `stdin`. Usually, part 1 and part 2 of a given task are in
separate files `part1.py` and `part2.py`, but there are exceptions with both
parts in `both.py`. As the authors of AoC do not wish the participants to share
their input files, I only include small test files which are usually those from
the task description.

To run, for example, the solution to part 2 of the task 2022/03 on the small
test input, use:
```
poetry run python3 2022/03/part2.py < 2022/03/test.in
```

Test can be run with:
```
poetry run pytest
```

## Some notes about the AoC years

### 2022

You can see me in [Top 100 of Part 1 on day 10](https://adventofcode.com/2022/leaderboard/day/10)

_Day 11:_ The monkeys with crazily growing numbers.

_Day 15:_ Intersections of balls in the Manhattan metric. I managed to write a
fast solution, but I would not like to prove its correctness.

_Day 16:_ The solution of part 2 runs for a little over a minute on my actual
input on my laptop. I don't have a much faster solution.

_Day 17:_ Tetris simulation. My solution of part 2 is a bit heuristic.
