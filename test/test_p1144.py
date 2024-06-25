"""Test for Beecrowd exercise 1144."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1144 import main as p1144


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "5\n",
            (
                "1 1 1\n"
                "1 2 2\n"
                "2 4 8\n"
                "2 5 9\n"
                "3 9 27\n"
                "3 10 28\n"
                "4 16 64\n"
                "4 17 65\n"
                "5 25 125\n"
                "5 26 126\n"
            )
        ),
    ]
)
def test_exercise_1144(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1144."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1144()

    captured = capfd.readouterr()

    assert captured.out == expected_output
