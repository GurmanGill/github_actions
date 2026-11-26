import pytest

from src.calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, 2, 0),
        (0, 0, 0),
    ],
)
def test_add_multiple_values(a, b, expected):
    assert add(a, b) == expected
