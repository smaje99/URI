"""Test for Beecrowd exercise 1030."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1030 import main as p1030


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3\n5 2\n6 3\n1234 233\n",
            "Case 1: 3\nCase 2: 1\nCase 3: 25\n",
        ),
    ],
)
def test_exercise_1030(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1030."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1030()

    captured = capfd.readouterr()

    assert captured.out == expected_output
