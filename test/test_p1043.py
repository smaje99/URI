"""Test for Beecrowd exercise 1040."""

from typing import Any
from io import StringIO
import sys

import pytest

from python.p1043 import main as p1043


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ("6.0 4.0 2.0\n", "Area = 10.0\n"),
        ("6.0 4.0 2.1\n", "Perimetro = 12.1\n"),
    ],
)
def test_exercise_1043(capfd: Any, input_values: str, expected_output: str):
    """Test for Beecrowd exercise 1043."""
    sys.stdin = StringIO(input_values)

    p1043()

    output = capfd.readouterr()[0]

    assert output == expected_output
