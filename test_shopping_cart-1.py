import unittest
from ShoppingCart import Product  
from ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = Product("Apple", 1.0, 5)
        self.product2 = Product("Banana", 0.5, 10)

    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Apple")
        print("test_add_product: Passed")

    def test_remove_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.remove_product("Apple")
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Banana")
        print("test_remove_product: Passed")

    def test_update_quantity(self):
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Apple", 10)
        self.assertEqual(self.cart.products[0].quantity, 10)
        print("test_update_quantity: Passed")

    def test_calculate_subtotal(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(self.cart.calculate_subtotal(), 10.0)
        print("test_calculate_subtotal: Passed")

    def test_set_tax_rate(self):
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.tax_rate, 0.08)
        print("test_set_tax_rate: Passed")

    def test_calculate_tax(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_tax(), 0.8)
        print("test_calculate_tax: Passed")

    def test_calculate_total(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_total(), 10.8)
        print("test_calculate_total: Passed")

    # My tests
    def test_is_cart_notempty(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertFalse(self.cart._is_cart_empty())
        print("test_is_cart_empty: Passed")

    def test_is_cart_empty(self):
        self.assertTrue(self.cart._is_cart_empty())
        print("test_is_cart_empty_empty: Passed")

    def test_invalid_tax_rate(self):
        self.assertRaises(ValueError, self.cart.set_tax_rate, 1.5)
        print("test_invalid_tax_rate: Passed")

    def test_invalid_calculate_tax(self):
        self.assertRaises(Exception, self.cart.calculate_tax)
        print("test_invalid_calculate_tax: Passed")

    def test_no_product_found_remove(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.remove_product("Orange")
        self.assertEqual(len(self.cart.products), 2)
        print("test_no_product_found: Passed")

    def test_no_product_found_update(self):
        self.cart.add_product(self.product1)
        qty = self.product1.quantity
        self.cart.update_quantity("Orange", 10)
        self.assertEqual(self.cart.products[0].quantity, qty)
        print("test_no_product_found: Passed")

    


if __name__ == "__main__":
    unittest.main()
