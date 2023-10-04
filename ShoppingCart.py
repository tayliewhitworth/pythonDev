class Product:
    def __init__(self, name, price, quantity):
        # Initialize product attributes
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        # Initialize shopping cart attributes
        self.products = []
        self.tax_rate = 0.0

    def add_product(self, product):
        # Add a product to the cart
        self.products.append(product)

    def remove_product(self, product_name):
        # Remove a product from the cart by name
        product_to_remove = None
        for product in self.products:
            if product.name == product_name:
                product_to_remove = product
                break
        if product_to_remove is not None:
            self.products.remove(product_to_remove)
        else:
            print("Product not found in cart.")

    def update_quantity(self, product_name, new_quantity):
        # Update the quantity of a product in the cart
        product_to_update = None
        for product in self.products:
            if product.name == product_name:
                product_to_update = product
                break
        if product_to_update is not None:
            product_to_update.quantity = new_quantity
        else:
            print("Product not found in cart.")

    def calculate_subtotal(self):
        # Calculate the subtotal of items in the cart
        subtotal = 0
        if self._is_cart_empty():
            return 0
        for product in self.products:
            subtotal += product.price * product.quantity
        return subtotal

    def set_tax_rate(self, tax_rate):
        # Set the tax rate for the cart
        if not (isinstance(tax_rate, float) and 0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be a decimal between 0 and 1.")
        self.tax_rate = tax_rate

    def calculate_tax(self):
        # Calculate the total tax amount
        if self.tax_rate <= 0:
            raise Exception("Tax rate has not been set.")
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        # Calculate the total cost (subtotal + total tax)
        if self._is_cart_empty():
            return 0
        return self.calculate_subtotal() + self.calculate_tax()

    def display_cart(self):
        # Display all items in the cart with names, prices, and quantities
        print("-" * 50)
        print("Items in cart:")
        if self._is_cart_empty():
            return
        else:
            for product in self.products:
                print(f"\nProduct: {product.name:<15} Price: ${product.price:.2f}\tQty: {product.quantity}")

    def _is_cart_empty(self):
        # Return True if the cart is empty
        if not self.products:
            print("Cart is empty. Add some items!")
            return True
        return False

def main():
    # Create a ShoppingCart object
    shopping_cart = ShoppingCart()

    while True:
        print("\nShopping Cart Menu")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Update product quantity")
        print("4. Show all items in cart")
        print("5. Calculate total cost")
        print("6. Set tax rate")
        print("7. Calculate total tax")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add product to cart
            product_name = input("Enter product name: ")
            while True:
                try:
                    product_price = float(input("Enter product price: "))
                    product_quantity = int(input("Enter product quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

            product = Product(product_name, product_price, product_quantity)
            shopping_cart.add_product(product)

        elif choice == '2':
            # Remove product from cart
            if shopping_cart._is_cart_empty():
                continue
            product_name = input("Enter product name to remove: ")
            shopping_cart.remove_product(product_name)
            shopping_cart.display_cart()

        elif choice == '3':
            # Update product quantity
            if shopping_cart._is_cart_empty():
                continue
            product_name = input("Enter product name to update: ")
            while True:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            shopping_cart.update_quantity(product_name, new_quantity)
            shopping_cart.display_cart()

        elif choice == '4':
            # Display all items in cart
            shopping_cart.display_cart()

        elif choice == '5':
            # Calculate and display total cost
            if shopping_cart.tax_rate <= 0:
                print("Tax rate has not been set.")
                while True:
                    try:
                        tax_rate = float(input("Enter tax rate as a decimal (0.08 for 8%): "))
                        shopping_cart.set_tax_rate(tax_rate)
                        break
                    except ValueError:
                        print("Invalid tax rate. Please enter a decimal between 0 and 1.")
            total_cost = shopping_cart.calculate_total()
            print(f"Total cost: ${total_cost:.2f}")

        elif choice == '6':
            # Set tax rate
            while True:
                try:
                    tax_rate = float(input("Enter tax rate as a decimal (0.08 for 8%): "))
                    if 0 <= tax_rate <= 1:
                        break
                    else:
                        print("Tax rate must be between 0 and 1.")
                except ValueError:
                    print("Invalid tax rate. Please try again.")
            shopping_cart.set_tax_rate(tax_rate)

        elif choice == '7':
            # Calculate and display total tax
            if shopping_cart.tax_rate <= 0:
                print("Tax rate has not been set.")
                while True:
                    try:
                        tax_rate = float(input("Enter tax rate as a decimal (0.08 for 8%): "))
                        shopping_cart.set_tax_rate(tax_rate)
                        break
                    except ValueError:
                        print("Invalid tax rate. Please enter a decimal between 0 and 1.")

            try:
                total_tax = shopping_cart.calculate_tax()
                print(f"\nTotal tax: ${total_tax:.2f}")
            except Exception as e:
                print(e)

        elif choice == '8':
            print("Exiting the Shopping Cart.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
