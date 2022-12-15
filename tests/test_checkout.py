from decimal import Decimal

import pytest

from checkout import Checkout, PRICES


@pytest.fixture()
def checkout():
    return Checkout()

@pytest.fixture()
def price_of_a():
    return PRICES['a']

@pytest.fixture()
def price_of_b():
    return PRICES['b']

@pytest.fixture()
def price_of_c():
    return PRICES['c']

# Single items

def test_one_a_costs_50(checkout, price_of_a):
    basket = {
        'a': 1,
    }
    assert checkout.total(basket) == price_of_a

def test_one_b_costs_30(checkout, price_of_b):
    basket = {
        'b': 1,
    }
    assert checkout.total(basket) == price_of_b

def test_one_c_costs_10(checkout, price_of_c):
    basket = {
        'c': 1,
    }
    assert checkout.total(basket) == price_of_c

# Multiple items

def test_two_a_costs_100(checkout, price_of_a):
    basket = {
        'a': 2,
    }
    assert checkout.total(basket) == price_of_a * 2

# Discounts

def test_three_a_costs_130(checkout):
    basket = {
        'a': 3,
    }
    assert checkout.total(basket) == Decimal(130)

def test_nine_a_costs_390(checkout):
    basket = {
        'a': 9,
    }
    assert checkout.total(basket) == Decimal(390)

def test_ten_a_costs_440(checkout):
    basket = {
        'a': 10,
    }
    assert checkout.total(basket) == Decimal(440)


def test_two_b_costs_45(checkout):
    basket = {
        'b': 2,
    }
    assert checkout.total(basket) == Decimal(45)
