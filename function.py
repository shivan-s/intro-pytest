# function.py


class Maths:
    """
    A Maths class
        n (int) - starting interger value
    """

    def __init__(self, n: int):
        self.n = n

    def add(self, x: int) -> int:
        self.n += x
        return self.n

    def subtract(self, x: int) -> int:
        self.n -= x
        return self.n

    def __repr__(self):
        return f"n is {self.n}"
