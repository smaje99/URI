"""Test for Beecrowd exercise 1155."""

import pytest
from pytest import CaptureFixture

from python.p1155 import main as p1155


@pytest.mark.parametrize("expected_output", ["5.19\n"])
def test_exercise_1155(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1155."""
    p1155()

    captured = capfd.readouterr()

    assert captured.out == expected_output
