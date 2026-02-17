from app.calculation.calculation import Calculation
from app.operation.add import Add
from app.operation.subtract import Subtract
from app.operation.multiply import Multiply
from app.operation.divide import Divide


class CalculationFactory:
    operations = {
        "add": Add,
        "sub": Subtract,
        "mul": Multiply,
        "div": Divide
    }

    @staticmethod
    def create(operation, a, b):
        if operation not in CalculationFactory.operations:
            raise ValueError("Invalid operation")
        return Calculation(a, b, CalculationFactory.operations[operation])
