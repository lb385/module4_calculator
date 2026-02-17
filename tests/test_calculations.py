import pytest
from app.calculation.factory import CalculationFactory
from app.calculation.calculation import Calculation
from app.calculator.history import History


def test_factory_and_compute():
    calc = CalculationFactory.create('add', 1, 2)
    assert isinstance(calc, Calculation)
    assert calc.compute() == 3


def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create('mod', 1, 2)


def test_history_records():
    history = History()
    calc = CalculationFactory.create('mul', 3, 4)
    result = calc.compute()
    history.add(calc, result)
    assert history.show() == [(calc, result)]
