"""Test for Beecrowd exercise 1157."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1157 import main as p1157


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "6",
            "1\n2\n3\n6\n",
        ),
    ],
)
def test_exercise_1157(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1157."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1157()

    captured = capfd.readouterr()

    assert captured.out == expected_output
