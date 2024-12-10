from collections import Counter


def similarity_between_lists(input: list[list[int]]) -> int:
    """Calculate similarity between inputs.

    For each value in the first list, multiply by the count of times
    it appears in the second list.

    """
    counts = Counter(input[1])

    total = 0

    for value in input[0]:
        total += value * counts[value]

    return total
