# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from AAP_LAB_TASKS.materialy.lab_03.product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    # TODO: Zwroc instancje Product, np. Product("Laptop", 2999.99, 10)
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    # TODO: Uzyj assert product.is_available() == True
    assert product.is_available()


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    # TODO: Uzyj assert product.total_value() == oczekiwana_wartosc
    assert product.total_value() == product.quantity * product.price


# --- Testy z parametryzacja ---
@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),     # dodanie 5 do poczatkowych 10 = 15
    (0, 10),     # dodanie 0 = bez zmian
    (100, 110),  # dodanie 100
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(product.quantity + 1)


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-5)