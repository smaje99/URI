"""Test for Beecrowd exercise 1531."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p1531 import main as p1531


@pytest.mark.parametrize(
  "input_data, expected_output",
  [
    (
      (
        "1 100\n"
        "2 100\n"
        "3 100\n"
        "4 100\n"
        "5 100\n"
        "5 2\n"
        "6 100\n"
      ),
      "1\n1\n1\n2\n5\n1\n21\n",
    ),
    (
      (
        "1000000000 1000000\n"
        "999999937 999983\n"
        "123456789 98765\n"
        "111111111 2\n"
      ),
      "781250\n230327\n27537\n1\n",
    ),
  ],
)
def test_exercise_2413(
  monkeypatch: MonkeyPatch,
  capfd: CaptureFixture[str],
  input_data: str,
  expected_output: str,
):
  """Test for Beecrowd exercise 1531."""
  monkeypatch.setattr(sys, "stdin", StringIO(input_data))

  p1531()

  captured = capfd.readouterr()

  assert captured.out == expected_output
