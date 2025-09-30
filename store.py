from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products if p.is_active())

    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    order_price = best_buy.order([
        (products[0], 1),
        (products[1], 2)
    ])
    print(f"Order cost: {order_price} dollars")