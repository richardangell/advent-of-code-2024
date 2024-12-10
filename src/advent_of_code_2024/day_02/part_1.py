def check_report_is_safe(report: list[int]) -> bool:
    """Check a single report is safe.

    Must be monotonically increasing or decreasing and adjacent values must differ
    by between one and three.

    """
    increasing = report[1] > report[0]

    previous_value = report[0]

    for next_value in report[1:]:
        within_range = (
            previous_value + 1 <= next_value <= previous_value + 3
            if increasing
            else previous_value - 1 >= next_value >= previous_value - 3
        )

        if not within_range:
            return False

        previous_value = next_value

    return True


def count_safe_reports(reports: list[list[int]]) -> int:
    """Count number of safe reports from list."""
    count = 0

    for report in reports:
        if check_report_is_safe(report):
            count += 1

    return count
