from decimal import Decimal

PRICES = {
    'A'.lower(): Decimal(50),
    'B'.lower(): Decimal(30),
    'C'.lower(): Decimal(10),
}

class Checkout():
    def __init__(self):
        pass

    def total(self, basket):
        return Decimal()
