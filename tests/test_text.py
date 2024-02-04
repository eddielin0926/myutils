from myutils import text


def test_percent():
    assert text.fpercent(1, 3) == "33.33%"


def test_wrap():
    assert text.wrap([1, 2, 3, 4, 5]) == "[1, 2, ..., 5]"
