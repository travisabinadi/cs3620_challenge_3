class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value + other.value