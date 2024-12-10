def distance_between_lists(input: list[list[int]]) -> int:
    """Calculate absolute difference between sorted lists."""
    list_a = sorted(input[0])
    list_b = sorted(input[1])

    total = 0

    for a, b in zip(list_a, list_b, strict=False):
        total += abs(a - b)

    return total
