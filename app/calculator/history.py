class History:
    def __init__(self):
        self.records = []

    def add(self, calculation, result):
        self.records.append((calculation, result))

    def show(self):
        return self.records
