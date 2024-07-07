"""Test for Beecrowd exercise 1154."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1154 import main as p1154


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "34\n56\n44\n23\n-2\n",
            "39.25\n",
        ),
    ],
)
def test_exercise_1154(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1154."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1154()

    captured = capfd.readouterr()

    assert captured.out == expected_output
