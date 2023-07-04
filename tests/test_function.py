# test_function.py
import pytest

from function import Maths


@pytest.fixture
def maths():
    return Maths(10)


def test_exists(maths):
    """
    Checks if objects are created
    """
    assert isinstance(maths, Maths)


def test_add(maths):
    """
    Addition method
    """
    assert maths.add(10) == 20


def test_subtract(maths):
    """
    Subtraction method
    """
    assert maths.subtract(5) == 5
