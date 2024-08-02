"""Test for Beecrowd exercise 2413."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p2413 import main as p2413


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2\n", "8\n"),
        ("25\n", "100\n"),
    ],
)
def test_exercise_2413(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 2413."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p2413()

    captured = capfd.readouterr()

    assert captured.out == expected_output
