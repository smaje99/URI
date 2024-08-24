"""Test for Beecrowd exercise 1160."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1160 import main as p1160


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            (
                "6\n"
                "100 150 1.0 0\n"
                "90000 120000 5.5 3.5\n"
                "56700 72000 5.2 3.0\n"
                "123 2000 3.0 2.0\n"
                "100000 110000 1.5 0.5\n"
                "62422 484317 3.1 1.0\n"
            ),
            (
                "51 anos.\n"
                "16 anos.\n"
                "12 anos.\n"
                "Mais de 1 seculo.\n"
                "10 anos.\n"
                "100 anos.\n"
            ),
        )
    ],
)
def test_exercise_1160(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1160."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1160()

    captured = capfd.readouterr()

    assert captured.out == expected_output
