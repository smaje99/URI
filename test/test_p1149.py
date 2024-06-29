"""Test for Beecrowd exercise 1149."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1149 import main as p1149


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3 2\n",
            "7\n",
        ),
    ],
)
def test_exercise_1149_1(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1149."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1149()

    captured = capfd.readouterr()

    assert captured.out == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3 -1 0 -2 2\n",
            "7\n",
        ),
    ],
)
def test_exercise_1149_2(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1149."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1149()

    captured = capfd.readouterr()

    assert captured.out == expected_output
