import subprocess

import pytest

YEAR = 2022


@pytest.mark.parametrize(
    'task,src,in_,out',
    [
        [1, 'part1.py', 'test.in', 'test_part1.out'],
        [1, 'part2.py', 'test.in', 'test_part2.out'],
        [2, 'part1.py', 'test.in', 'test_part1.out'],
        [2, 'part2.py', 'test.in', 'test_part2.out'],
        [3, 'part1.py', 'test.in', 'test_part1.out'],
        [3, 'part2.py', 'test.in', 'test_part2.out'],
        [4, 'part1.py', 'test.in', 'test_part1.out'],
        [4, 'part2.py', 'test.in', 'test_part2.out'],
        [5, 'part1.py', 'test.in', 'test_part1.out'],
        [5, 'part2.py', 'test.in', 'test_part2.out'],
        [6, 'part1.py', 'test.in', 'test_part1.out'],
        [6, 'part2.py', 'test.in', 'test_part2.out'],
        [7, 'part1.py', 'test.in', 'test_part1.out'],
        [7, 'part2.py', 'test.in', 'test_part2.out'],
        [8, 'part1.py', 'test.in', 'test_part1.out'],
        [8, 'part2.py', 'test.in', 'test_part2.out'],
        [9, 'part1.py', 'test1.in', 'test1_part1.out'],
        [9, 'part2.py', 'test2.in', 'test2_part2.out'],
        [10, 'part1.py', 'test.in', 'test_part1.out'],
        [10, 'part2.py', 'test.in', 'test_part2.out'],
        [11, 'part1.py', 'test.in', 'test_part1.out'],
        [11, 'part2.py', 'test.in', 'test_part2.out'],
        [12, 'part1.py', 'test.in', 'test_part1.out'],
        [12, 'part2.py', 'test.in', 'test_part2.out'],
        [13, 'both.py', 'test.in', 'test_both.out'],
        [14, 'part1.py', 'test.in', 'test_part1.out'],
        [14, 'part2.py', 'test.in', 'test_part2.out'],
        [15, 'part1.py', 'test.in', 'test_part1.out'],
        [15, 'part2.py', 'test.in', 'test_part2.out'],
        [16, 'part1.py', 'test.in', 'test_part1.out'],
        [16, 'part2.py', 'test.in', 'test_part2.out'],
        [17, 'part1.py', 'test.in', 'test_part1.out'],
        [17, 'part2.py', 'test.in', 'test_part2.out'],
        [18, 'part1.py', 'test.in', 'test_part1.out'],
        [18, 'part2.py', 'test.in', 'test_part2.out'],
        [20, 'part1.py', 'test.in', 'test_part1.out'],
        [20, 'part2.py', 'test.in', 'test_part2.out'],
        [21, 'part1.py', 'test.in', 'test_part1.out'],
        [21, 'part2.py', 'test.in', 'test_part2.out'],
        [22, 'part1.py', 'test.in', 'test_part1.out'],
        [23, 'both.py', 'test.in', 'test_both.out'],
        [24, 'both.py', 'test.in', 'test_both.out'],
    ],
)
def test_inputs(task, src, in_, out):
    with open(f'{YEAR}/{task:02}/{out}') as f:
        expected_output = f.read()
    with open(f'{YEAR}/{task:02}/{in_}') as f:
        output = subprocess.run(
            ['poetry', 'run', 'python3', f'{YEAR}/{task:02}/{src}'],
            stdin=f,
            capture_output=True,
        )
    assert output.stdout.decode() == expected_output
