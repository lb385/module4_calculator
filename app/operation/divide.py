class Divide:
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
