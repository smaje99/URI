"""Test for Beecrowd exercise 1113."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.bee1113 import main as bee1113


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "5 4\n7 2\n3 8\n2 2\n",
            "Decrescente\nDecrescente\nCrescente\n",
        ),
    ],
)
def test_exercise_1113(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1113."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    bee1113()

    captured = capfd.readouterr()

    assert captured.out == expected_output
