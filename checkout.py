from decimal import Decimal

DISCOUNTS = {
    'A'.lower(): {
        'condition': lambda x: x >= 3,
        'count': 3,
        'price': Decimal(130),
        },
    'B'.lower(): {
        'condition': lambda x: x >= 2,
        'count': 2,
        'price': Decimal(45),
        },
}

PRICES = {
    'A'.lower(): Decimal(50),
    'B'.lower(): Decimal(30),
    'C'.lower(): Decimal(10),
}

class Checkout():
    def __init__(self):
        pass

    def _is_discounted(self, sku, count):
        try:
            return DISCOUNTS[sku]['condition'](count)
        except KeyError:
            return False

    def total(self, basket):
        total = Decimal(0)
        for sku, count in basket.items():
            if self._is_discounted(sku, count):
                pass
            else:
                total += PRICES[sku] * count
        return total
