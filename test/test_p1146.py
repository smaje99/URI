"""Test for Beecrowd exercise 1146."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1146 import main as p1146


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "5\n10\n3\n0\n",
            (
                "1 2 3 4 5\n"
                "1 2 3 4 5 6 7 8 9 10\n"
                "1 2 3\n"
            )
        ),
    ]
)
def test_exercise_1146(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1146."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1146()

    captured = capfd.readouterr()

    assert captured.out == expected_output
