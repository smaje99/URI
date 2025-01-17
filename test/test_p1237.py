"""Test for Beecrowd exercise 1237."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1237 import main as p1237


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            (
                "twoequalnames\n"
                "twoequalnames"
            ),
            "13\n"
        ),
        (
            (
                "Find the longest common substring\n"
                "The substring can be any part of the String\n"
                "If there is no common substring, return 0\n"
                "The search is case sensitive"
            ),
            "10\n4\n"
        ),
        (
            (
                "abcdef\n"
                "cdofhij\n"
                "TWO\n"
                "FOUR\n"
                "abracadabra\n"
                "open\n"
                "Hey This java is hot\n"
                "Java is a new paradigm"
            ),
            "2\n1\n0\n7\n"
        )
    ],
)
def test_exercise_1237(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1237."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1237()

    captured = capfd.readouterr()

    assert captured.out == expected_output
