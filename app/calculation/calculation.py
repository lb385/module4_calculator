class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def compute(self):
        return self.operation.execute(self.a, self.b)
