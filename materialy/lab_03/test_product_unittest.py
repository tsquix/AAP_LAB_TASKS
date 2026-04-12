# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from AAP_LAB_TASKS.materialy.lab_03.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-15)

    def test_remove_stock_positive(self):
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_too_much_raises(self):
        # TODO: Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.remove_stock(30)

    def test_is_available_when_in_stock(self):
        # TODO: Uzyj self.assertTrue
        self.assertTrue(self.product.is_available)

    def test_is_not_available_when_empty(self):
        # TODO: Stworz produkt z quantity=0, uzyj self.assertFalse
        self.product = Product("Lapek", 2999.99, 0)
        self.assertFalse(self.product.is_available())

    def test_total_value(self):
        # TODO: Uzyj self.assertEqual
        total = self.product.price * self.product.quantity
        self.assertEqual(total, self.total_value())
        pass


if __name__ == "__main__":
    unittest.main()