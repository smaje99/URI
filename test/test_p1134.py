"""Test for Beecrowd exercise 1134."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1134 import main as p1134


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "8\n1\n7\n2\n2\n4\n",
            (
                "MUITO OBRIGADO\n"
                "Alcool: 1\n"
                "Gasolina: 2\n"
                "Diesel: 0\n"
            )
        ),
    ]
)
def test_exercise_1134(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1134."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1134()

    captured = capfd.readouterr()

    assert captured.out == expected_output
