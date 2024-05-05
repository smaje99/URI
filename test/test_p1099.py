"""Test for Beecrowd exercise 1099."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1099 import main as p1099


@pytest.mark.parametrize("input_data, expected_output", [
    (
        (
            "7\n"
            "4 5\n"
            "13 10\n"
            "6 4\n"
            "3 3\n"
            "3 5\n"
            "3 4\n"
            "3 8\n"
        ),
        "0\n11\n5\n0\n0\n0\n12\n",
    ),
])
def test_exercise_1099(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1099."""
    # Usamos monkeypatch para redirigir la entrada estándar
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1099()

    captured = capfd.readouterr()

    assert captured.out == expected_output
