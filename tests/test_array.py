from myutils import array


def test_flatten():
    assert array.flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_unique():
    assert array.unique([1, 1, 1]) == [1]
