import pytest
import collections

from .utils import possible_lower_and_upper_case_permutations


def test_combination_function():
    test_one = possible_lower_and_upper_case_permutations("a2B")
    assert collections.Counter(test_one) == collections.Counter(
        [
            "a2b",
            "a2B",
            "A2b",
            "A2B",
        ]
    )
