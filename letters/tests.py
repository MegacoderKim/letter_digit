import pytest
import collections
from django.urls import reverse
from rest_framework.test import APIClient
from .utils import possible_lower_and_upper_case_variations


def test_combination_function():
    test_one = possible_lower_and_upper_case_variations("a2B")
    assert collections.Counter(test_one) == collections.Counter(
        [
            "a2b",
            "a2B",
            "A2b",
            "A2B",
        ]
    )


def test_posting_word_returns_variations():
    client = APIClient()
    response = client.post(reverse("wordvariations"), {"word": "a2B"}, format="json")
    assert response.status_code == 200
