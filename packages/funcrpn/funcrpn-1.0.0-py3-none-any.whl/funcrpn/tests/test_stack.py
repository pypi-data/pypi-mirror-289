"Unit test"

from funcrpn import stack


def test_push():
    "Unit test"
    assert stack.push([1, 2, 3], 4) == [1, 2, 3, 4]


def test_pop():
    "Unit test"
    assert stack.pop([1, 2, 3, 4]) == ([1, 2, 3], 4)
