"""Test for Beecrowd exercise 1096."""

import pytest
from pytest import CaptureFixture

from python.p1096 import main as p1096


@pytest.mark.parametrize("expected_output", [(
  'I=1 J=7\n'
  'I=1 J=6\n'
  'I=1 J=5\n'
  'I=3 J=7\n'
  'I=3 J=6\n'
  'I=3 J=5\n'
  'I=5 J=7\n'
  'I=5 J=6\n'
  'I=5 J=5\n'
  'I=7 J=7\n'
  'I=7 J=6\n'
  'I=7 J=5\n'
  'I=9 J=7\n'
  'I=9 J=6\n'
  'I=9 J=5\n'
)])
def test_exercise_1096(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1096."""
    p1096()

    captured = capfd.readouterr()

    assert captured.out == expected_output
