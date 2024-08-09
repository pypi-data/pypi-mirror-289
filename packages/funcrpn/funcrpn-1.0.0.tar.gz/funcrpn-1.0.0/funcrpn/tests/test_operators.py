"Unit tests"
import pytest
from funcrpn import operators


def test_add():
    "Unit test"
    assert operators.add([1, 2, 3]) == [1, 5]


def test_sub():
    "Unit test"
    assert operators.sub([1, 2, 3]) == [1, -1]


def test_mul():
    "Unit test"
    assert operators.mul([1, 2, 3]) == [1, 6]


def test_div():
    "Unit test"
    assert operators.div([1, 2, 3]) == [1, 0.66666666666666666666]


def test_zero_division_error():
    "Unit test"
    with pytest.raises(ZeroDivisionError):
        operators.div([1, 0])


def test_power():
    "Unit test"
    assert operators.power([1, 2, 3]) == [1, 8]


def test_sqrt():
    "Unit test"
    assert operators.sqrt([1, 2, 4]) == [1, 2, 2]
