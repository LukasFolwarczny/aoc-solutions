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
