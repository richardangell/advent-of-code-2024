def check_report_is_safe_with_tolerance(
    report: list[int], allow_single_failure: bool = True
) -> bool:
    """Check a single report is safe allowing for one failing pair of values.

    Must be monotonically increasing or decreasing and adjacent values must differ
    by between one and three.

    """
    if len(report) == 1:
        return True
    elif len(report) == 0:
        return False

    increasing = report[1] > report[0]

    previous_value = report[0]

    for previous_index, next_value in enumerate(report[1:]):
        before_previous_index = previous_index - 1
        next_index = previous_index + 1

        within_range = (
            previous_value + 1 <= next_value <= previous_value + 3
            if increasing
            else previous_value - 1 >= next_value >= previous_value - 3
        )

        if not within_range:
            # at the first failure try removing each value by itself from report
            if allow_single_failure:
                report_next_value_removed = report[:]
                del report_next_value_removed[next_index]

                safe_without_next_value = check_report_is_safe_with_tolerance(
                    report=report_next_value_removed,
                    allow_single_failure=False,
                )

                report_previous_value_removed = report[:]
                del report_previous_value_removed[previous_index]

                safe_without_previous_value = check_report_is_safe_with_tolerance(
                    report=report_previous_value_removed,
                    allow_single_failure=False,
                )

                if before_previous_index >= 0:
                    report_two_previous_value_removed = report[:]
                    del report_two_previous_value_removed[before_previous_index]

                    safe_without_two_previous_value = (
                        check_report_is_safe_with_tolerance(
                            report=report_two_previous_value_removed,
                            allow_single_failure=False,
                        )
                    )

                else:
                    safe_without_two_previous_value = False

                return (
                    safe_without_two_previous_value
                    or safe_without_previous_value
                    or safe_without_next_value
                )

            else:
                return False

        previous_value = next_value

    return True


def count_safe_reports_with_tolerance(reports: list[list[int]]) -> int:
    """Count number of safe reports from list tolerating one failure per report."""
    count = 0

    for report in reports:
        if check_report_is_safe_with_tolerance(report):
            count += 1

    return count
