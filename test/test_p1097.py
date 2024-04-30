"""Test for Beecrowd exercise 1097."""

import pytest
from pytest import CaptureFixture

from python.p1097 import main as p1097


@pytest.mark.parametrize("expected_output", [(
  'I=1 J=7\n'
  'I=1 J=6\n'
  'I=1 J=5\n'
  'I=3 J=9\n'
  'I=3 J=8\n'
  'I=3 J=7\n'
  'I=5 J=11\n'
  'I=5 J=10\n'
  'I=5 J=9\n'
  'I=7 J=13\n'
  'I=7 J=12\n'
  'I=7 J=11\n'
  'I=9 J=15\n'
  'I=9 J=14\n'
  'I=9 J=13\n'
)])
def test_exercise_1097(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1097."""
    p1097()

    captured = capfd.readouterr()

    assert captured.out == expected_output
