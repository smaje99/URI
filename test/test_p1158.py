"""Test for Beecrowd exercise 1158."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1158 import main as p1158


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "4\n4 3\n11 2\n4 5\n7 4\n",
            "21\n24\n45\n40\n",
        ),
    ],
)
def test_exercise_1158(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1158."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1158()

    captured = capfd.readouterr()

    assert captured.out == expected_output
