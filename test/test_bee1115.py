"""Test for Beecrowd exercise 1115."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.bee1115 import main as bee1115


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "2 2\n3 -2\n-8 -1\n-7 1\n0 2\n",
            "primeiro\nquarto\nterceiro\nsegundo\n",
        ),
    ],
)
def test_exercise_1115(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1115."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    bee1115()

    captured = capfd.readouterr()

    assert captured.out == expected_output
