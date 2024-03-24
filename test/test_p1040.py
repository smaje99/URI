"""Test for Beecrowd exercise 1040."""

from typing import Any
from io import StringIO
import sys

import pytest

from python.p1040 import main as p1040


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        (
            ("2.0 4.0 7.5 8.0\n6.4\n",),
            "Media: 5.4\nAluno em exame.\nNota do exame: 6.4\n"
            + "Aluno aprovado.\nMedia final: 5.9\n",
        ),
        (("2.0 6.5 4.0 9.0\n",), "Media: 4.8\nAluno reprovado.\n"),
        (("9.0 4.0 8.5 9.0\n",), "Media: 7.3\nAluno aprovado.\n"),
    ],
)
def test_exercise_p_1040(
  capfd: Any, input_values: tuple[str], expected_output: str
):
    """Test for Beecrowd exercise 1040."""
    sys.stdin = StringIO(input_values[0])

    p1040()

    output = capfd.readouterr()[0]

    assert output == expected_output
