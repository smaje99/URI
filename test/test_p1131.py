"""Test for Beecrowd exercise 1131."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1131 import main as p1131


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3 2\n1\n2 3\n1\n3 1\n2\n",
            (
                "Novo grenal (1-sim 2-nao)\n"
                "Novo grenal (1-sim 2-nao)\n"
                "Novo grenal (1-sim 2-nao)\n"
                "3 grenais\n"
                "Inter:2\n"
                "Gremio:1\n"
                "Empates:0\n"
                "Inter venceu mais\n"
            ),
        ),
    ]
)
def test_exercise_1131_1(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1131."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1131()

    captured = capfd.readouterr()

    assert captured.out == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [(
        "1 4\n1\n2 1\n1\n9 9\n1\n1 1\n2\n",
        (
            "Novo grenal (1-sim 2-nao)\n"
            "Novo grenal (1-sim 2-nao)\n"
            "Novo grenal (1-sim 2-nao)\n"
            "Novo grenal (1-sim 2-nao)\n"
            "4 grenais\n"
            "Inter:1\n"
            "Gremio:1\n"
            "Empates:2\n"
            "Nao houve vencedor\n"
        ),
    )]
)
def test_exercise_1131_2(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 1131."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p1131()

    captured = capfd.readouterr()

    assert captured.out == expected_output
