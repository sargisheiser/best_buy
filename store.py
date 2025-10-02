from typing import List, Tuple
from products import Product


class Store:
    """
    Store that contains multiple products and allows operations like
    adding, removing, listing, and ordering products.
    """

    def __init__(self, products: List[Product]):
        """Initialize store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of all active products."""
        return sum(p.get_quantity() for p in self.products if p.is_active())

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Place an order based on a shopping list of (Product, quantity) tuples.
        Returns total price of the order.
        Validates that all products are active and in the store.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} is not available in this store.")
            if not product.is_active():
                raise RuntimeError(f"Product {product.name} is not active.")

            total_price += product.buy(quantity)
        return total_price
