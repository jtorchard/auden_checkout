from decimal import Decimal
from math import floor

DISCOUNTS = {
    'A'.lower(): {
        'condition': lambda x: x >= 3,
        'count': Decimal(3),
        'price': Decimal(130),
        },
    'B'.lower(): {
        'condition': lambda x: x >= 2,
        'count': Decimal(2),
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
            sku = sku.lower()
            if self._is_discounted(sku, count):
                discount_threshold = DISCOUNTS[sku]['count']
                discount_price = DISCOUNTS[sku]['price']
                remainder = count % discount_threshold
                if remainder == 0:
                    total += (count / discount_threshold) * discount_price
                else:
                    total += floor((count / discount_threshold)) * discount_price
                    total += PRICES[sku] * remainder
            else:
                total += PRICES[sku] * count
        return total
