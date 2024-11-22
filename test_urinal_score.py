from urinal_score import find_best_urinal
import pytest


def test():
    test_cases = [
        ([0], 0),  # 1
        ([1], -1),  # 2
        ([0, 0, 0, 0, 0], 0),  # 3
        ([1, 1, 1, 1, 1], -1),  # 4
        ([1, 0, 1, 0, 1], 1),  # 5
        ([0, 1, 0, 1, 0], 0),  # 6
        ([0, 1, 1, 1, 1], 0),  # 7
        ([1, 1, 1, 1, 0], 4),  # 8
        ([0, 1, 1, 1, 0], 0),  # 9
        ([1, 0, 0, 1], 1),  # 10
        ([1, 0, 0, 0, 1], 2),  # 11
        ([1, 0, 0, 0, 0, 1], 2),  # 12
        ([1, 0, 1, 0, 0, 1], 3),  # 13
        ([1, 0, 0, 0, 1, 0, 0, 1], 2),  # 14
        ([1, 0, 0, 0, 0, 0, 0], 6),  # 15
        ([1, 0, 0, 0, 0, 1], 2),  # 16
    ]

    for i, (urinals, expected) in enumerate(test_cases):
        if i + 1 == 13:
            pass
        result = find_best_urinal(urinals)
        assert (
            result == expected
        ), f"Test case {i+1} failed: {urinals} → {result} (expected {expected})"
    print("All test cases passed!")
