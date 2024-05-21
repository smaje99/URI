"""Test for Beecrowd exercise 1101."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.bee1101 import main as bee1101


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "5 2\n6 3\n5 0\n",
            "2 3 4 5 Sum=14\n3 4 5 6 Sum=18\n",
        ),
    ],
)
def test_exercise_1101(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1101."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    bee1101()

    captured = capfd.readouterr()

    assert captured.out == expected_output
