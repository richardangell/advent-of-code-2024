import pytest

from advent_of_code_2024.day_02.part_1 import check_report_is_safe, count_safe_reports
from advent_of_code_2024.day_02.part_2 import (
    check_report_is_safe_with_tolerance,
    count_safe_reports_with_tolerance,
)
from advent_of_code_2024.helpers import load_row_input


@pytest.fixture(scope="session")
def case_1() -> list[list[int]]:
    return load_row_input("tests/day_02/case_1.txt")


@pytest.mark.parametrize(
    "row,expected",
    [
        (0, True),
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, True),
    ],
)
def test_check_report_is_safe(case_1, row, expected):
    result = check_report_is_safe(case_1[row])

    assert result is expected


@pytest.mark.parametrize(
    "file,expected",
    [
        ("tests/day_02/case_1.txt", 2),
        ("tests/day_02/input_1.txt", 534),
    ],
)
def test_part_1(file, expected):
    input = load_row_input(file)

    result = count_safe_reports(input)

    assert result == expected


@pytest.mark.parametrize(
    "row,expected",
    [
        (0, True),
        (1, False),
        (2, False),
        (3, True),
        (4, True),
        (5, True),
    ],
)
def test_check_report_is_safe_with_tolerance(case_1, row, expected):
    result = check_report_is_safe_with_tolerance(case_1[row])

    assert result is expected


@pytest.mark.parametrize(
    "report,expected",
    [
        ([35, 37, 39, 42, 43, 46, 48, 53], True),
        ([74, 75, 78, 81, 80, 83, 86, 90], False),
        ([67, 69, 71, 72, 75, 78, 76], True),
        ([10, 11, 9, 8], True),
        ([10, 11, 6, 5], False),
        ([10, 19, 9], True),
        ([10, 12, 19], True),
        ([10, 11, 16, 12], True),
        ([10, 16, 11, 12], True),
        ([17, 10, 11, 12], True),
        ([83, 86, 81, 78, 77, 75], True),
        ([71, 69, 70, 71, 72, 75], True),
    ],
)
def test_check_report_is_safe_with_tolerance_additional(report, expected):
    result = check_report_is_safe_with_tolerance(report)

    assert result is expected


@pytest.mark.parametrize(
    "file,expected",
    [
        ("tests/day_02/case_1.txt", 4),
        ("tests/day_02/input_1.txt", 577),
    ],
)
def test_part_2(file, expected):
    input = load_row_input(file)

    result = count_safe_reports_with_tolerance(input)

    assert result == expected
