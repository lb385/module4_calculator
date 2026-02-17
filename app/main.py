from app.calculation.factory import CalculationFactory
from app.calculator.history import History


def run():
    history = History()
    print("Calculator (type help for commands)")

    while True:
        cmd = input("Enter operation: ").lower()

        if cmd == "exit":
            print("Goodbye!")
            break

        if cmd == "help":
            print("Operations: add, sub, mul, div")
            print("Commands: history, exit")
            continue

        if cmd == "history":
            for c, r in history.show():
                op_name = getattr(c.operation, '__name__', str(c.operation))
                print(f"{c.a} {op_name} {c.b} = {r}")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calc = CalculationFactory.create(cmd, a, b)
            result = calc.compute()
            history.add(calc, result)

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run()
