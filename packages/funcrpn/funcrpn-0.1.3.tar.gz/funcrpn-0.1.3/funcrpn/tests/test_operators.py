from funcrpn import operators
import pytest


def test_add():
    assert operators.add([1, 2, 3]) == [1, 5]


def test_sub():
    assert operators.sub([1, 2, 3]) == [1, -1]


def test_mul():
    assert operators.mul([1, 2, 3]) == [1, 6]


def test_div():
    assert operators.div([1, 2, 3]) == [1, 0.66666666666666666666]


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        operators.div([1, 0])


def test_pow():
    assert operators.pow([1, 2, 3]) == [1, 8]


def test_sqrt():
    assert operators.sqrt([1, 2, 4]) == [1, 2, 2]
