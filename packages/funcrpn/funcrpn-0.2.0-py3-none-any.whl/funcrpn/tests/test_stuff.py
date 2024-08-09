"""Unit tests"""

import pytest
from funcrpn import __main__


def test_detect():
    "Unit test"
    assert __main__.detect_type("0.12333") == (0.12333, __main__.NUMBER)
    assert __main__.detect_type("3") == (3, __main__.NUMBER)
    assert __main__.detect_type("+") == ("+", __main__.OPERATOR)


def test_evaluate():
    "Unit test"
    assert __main__.evaluate([], 4) == [4]
    assert __main__.evaluate([1, 2, 3, 4], '+') == [1, 2, 7]
    assert __main__.evaluate([1, 2, 3, 4], '-') == [1, 2, -1]
    assert __main__.evaluate([1, 2, 3, 4], '*') == [1, 2, 12]
    assert __main__.evaluate([1, 2, 3, 4], '/') == [1, 2, 3 / 4]
    assert __main__.evaluate([1, 2, 3, 4], '^') == [1, 2, 81]
    assert __main__.evaluate([1, 2, 3, 4], 'sq') == [1, 2, 3, 2]


def test_error():
    with pytest.raises(__main__.NotACommandError):
        __main__.evaluate([], 'huh')
