"""Test for Beecrowd exercise 2374."""

from io import StringIO
import sys

import pytest
from pytest import MonkeyPatch, CaptureFixture

from python.p2374 import main as p2374


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "30\n18\n",
            "12\n",
        ),
    ],
)
def test_exercise_2374_1(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 2374."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p2374()

    captured = capfd.readouterr()

    assert captured.out == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "27\n27\n",
            "0\n",
        ),
    ],
)
def test_exercise_2374_2(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 2374."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p2374()

    captured = capfd.readouterr()

    assert captured.out == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "27\n30\n",
            "-3\n",
        ),
    ],
)
def test_exercise_2374_3(
    monkeypatch: MonkeyPatch,
    capfd: CaptureFixture[str],
    input_data: str,
    expected_output: str,
):
    """Test for Beecrowd exercise 2374."""
    monkeypatch.setattr(sys, "stdin", StringIO(input_data))

    p2374()

    captured = capfd.readouterr()

    assert captured.out == expected_output
