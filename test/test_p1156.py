"""Test for Beecrowd exercise 1156."""

import pytest
from pytest import CaptureFixture

from python.p1156 import main as p1156


@pytest.mark.parametrize("expected_output", ["6.00\n"])
def test_exercise_1156(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1156."""
    p1156()

    captured = capfd.readouterr()

    assert captured.out == expected_output
