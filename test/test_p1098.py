"""Test for Beecrowd exercise 1098."""

import pytest
from pytest import CaptureFixture

from python.p1098 import main as p1098


@pytest.mark.parametrize("expected_output", [(
  'I=0 J=1\n'
  'I=0 J=2\n'
  'I=0 J=3\n'
  'I=0.2 J=1.2\n'
  'I=0.2 J=2.2\n'
  'I=0.2 J=3.2\n'
  'I=0.4 J=1.4\n'
  'I=0.4 J=2.4\n'
  'I=0.4 J=3.4\n'
  'I=0.6 J=1.6\n'
  'I=0.6 J=2.6\n'
  'I=0.6 J=3.6\n'
  'I=0.8 J=1.8\n'
  'I=0.8 J=2.8\n'
  'I=0.8 J=3.8\n'
  'I=1 J=2\n'
  'I=1 J=3\n'
  'I=1 J=4\n'
  'I=1.2 J=2.2\n'
  'I=1.2 J=3.2\n'
  'I=1.2 J=4.2\n'
  'I=1.4 J=2.4\n'
  'I=1.4 J=3.4\n'
  'I=1.4 J=4.4\n'
  'I=1.6 J=2.6\n'
  'I=1.6 J=3.6\n'
  'I=1.6 J=4.6\n'
  'I=1.8 J=2.8\n'
  'I=1.8 J=3.8\n'
  'I=1.8 J=4.8\n'
  'I=2 J=3\n'
  'I=2 J=4\n'
  'I=2 J=5\n'
)])
def test_exercise_1098(capfd: CaptureFixture[str], expected_output: str):
    """Test for Beecrowd exercise 1098."""
    p1098()

    captured = capfd.readouterr()

    assert captured.out == expected_output
