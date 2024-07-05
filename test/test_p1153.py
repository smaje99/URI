"""Test for Beecrowd exercise 1153."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1153 import main as p1153


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "4\n",
            "24\n",
        ),
    ],
)
def test_exercise_1153(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1153."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1153()

    captured = capfd.readouterr()

    assert captured.out == expected_output
