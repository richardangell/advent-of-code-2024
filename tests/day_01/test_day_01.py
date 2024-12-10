import pytest

from advent_of_code_2024.day_01.part_1 import distance_between_lists
from advent_of_code_2024.day_01.part_2 import similarity_between_lists
from advent_of_code_2024.helpers import load_column_input


@pytest.mark.parametrize(
    "file,expected",
    [("tests/day_01/case_1.txt", 11), ("tests/day_01/input_1.txt", 1151792)],
)
def test_part_1(file, expected):
    input = load_column_input(file=file, line_separator="   ")

    result = distance_between_lists(input)

    assert result == expected


@pytest.mark.parametrize(
    "file,expected",
    [("tests/day_01/case_1.txt", 31), ("tests/day_01/input_1.txt", 21790168)],
)
def test_part_2(file, expected):
    input = load_column_input(file=file, line_separator="   ")

    result = similarity_between_lists(input)

    assert result == expected
