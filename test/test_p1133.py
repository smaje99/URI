"""Test for Beecrowd exercise 1133."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1133 import main as p1133


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "10\n18\n",
            "12\n13\n17\n"
        ),
    ]
)
def test_exercise_1133(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1133."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1133()

    captured = capfd.readouterr()

    assert captured.out == expected_output
