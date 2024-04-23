"""Test for Beecrowd exercise 1094."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1094 import main as p1094


@pytest.mark.parametrize("input_data, expected_output", [
    (
        "10\n10 C\n6 R\n15 S\n5 C\n14 R\n9 C\n6 R\n8 S\n5 C\n14 R\n",
        (
            "Total: 92 cobaias\n"
            "Total de coelhos: 29\n"
            "Total de ratos: 40\n"
            "Total de sapos: 23\n"
            "Percentual de coelhos: 31.52 %\n"
            "Percentual de ratos: 43.48 %\n"
            "Percentual de sapos: 25.00 %\n"
        )
    ),
])
def test_exercise_1094(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1094."""
    # Usamos monkeypatch para redirigir la entrada estándar
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1094()

    captured = capfd.readouterr()

    assert captured.out == expected_output
