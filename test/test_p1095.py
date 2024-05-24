"""Test for Beecrowd exercise 1095."""

import pytest
from pytest import CaptureFixture

from python.p1095 import main as p1095


@pytest.mark.parametrize("expected_output", [(
  'I=1 J=60\n'
  'I=4 J=55\n'
  'I=7 J=50\n'
  'I=10 J=45\n'
  'I=13 J=40\n'
  'I=16 J=35\n'
  'I=19 J=30\n'
  'I=22 J=25\n'
  'I=25 J=20\n'
  'I=28 J=15\n'
  'I=31 J=10\n'
  'I=34 J=5\n'
  'I=37 J=0\n'
)])
def test_exercise_1095(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1095."""
    p1095()

    captured = capfd.readouterr()

    assert captured.out == expected_output
