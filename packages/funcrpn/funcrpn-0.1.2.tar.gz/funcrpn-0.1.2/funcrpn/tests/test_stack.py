from funcrpn import stack


def test_push():
    assert stack.push([1, 2, 3], 4) == [1, 2, 3, 4]


def test_pop():
    assert stack.pop([1, 2, 3, 4]) == ([1, 2, 3], 4)
