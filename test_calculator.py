import pytest
from calculator import Calculator


def test_add():
    assert Calculator().add(2, 3) == 5


def test_minus():
    assert Calculator().minus(5, 3) == 2


def test_multiply():
    assert Calculator().multiply(4, 3) == 12


def test_divide():
    assert Calculator().divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator().divide(1, 0)