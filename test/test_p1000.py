'''Test for Beecrowd exercise 1000.'''

from typing import Any
import pytest

from python.p1000 import main as p1000


@pytest.mark.parametrize('expected_output', ['Hello World!\n'])
def test_exercise_p_1000(capsys: Any, expected_output: str):
    '''Test for Beecrowd exercise 1000.'''
    p1000()

    output = capsys.readouterr()[0]

    assert output == expected_output
