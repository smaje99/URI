"""Test for Beecrowd exercise 1150."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1150 import main as p1150


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3\n1\n20\n",
            "5\n",
        ),
    ],
)
def test_exercise_1150(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1150."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1150()

    captured = capfd.readouterr()

    assert captured.out == expected_output
