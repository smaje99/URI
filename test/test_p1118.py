"""Test for Beecrowd exercise 1118."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1118 import main as p1118


@pytest.mark.parametrize(
    "input_data, expected_output",
    [(
        "-3.5\n3.5\n11.0\n10.0\n4\n1\n8.0\n9.0\n2\n",
        (
            "nota invalida\n"
            "nota invalida\n"
            "media = 6.75\n"
            "novo calculo (1-sim 2-nao)\n"
            "novo calculo (1-sim 2-nao)\n"
            "media = 8.50\n"
            "novo calculo (1-sim 2-nao)\n"
        )
    )],
)
def test_exercise_1118(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: tuple[str],
):
    """Test for Beecrowd exercise 1118."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1118()

    captured = capfd.readouterr()

    assert captured.out == expected_output
