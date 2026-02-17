import pytest
from app.operation.add import Add
from app.operation.subtract import Subtract
from app.operation.multiply import Multiply
from app.operation.divide import Divide


@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, result):
    assert Add.execute(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (5, 3, 2),
    (0, 5, -5),
    (-1, -1, 0),
])
def test_subtract(a, b, result):
    assert Subtract.execute(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (2, 3, 6),
    (0, 5, 0),
    (-1, -1, 1),
])
def test_multiply(a, b, result):
    assert Multiply.execute(a, b) == result


def test_divide():
    assert Divide.execute(6, 3) == 2


def test_divide_zero():
    with pytest.raises(ValueError):
        Divide.execute(5, 0)
