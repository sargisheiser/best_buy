class Product:
    """
    Represents a product in the store with name, price, quantity, and active status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a product.
        Raises ValueError if name is empty or price/quantity are negative.
        """
        if not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Return the product quantity as float."""
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        """Set the product quantity and deactivate if it reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return product details as a string."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buy a certain quantity of the product.
        Returns total price. Raises exceptions if invalid.
        """
        if not self.active:
            raise RuntimeError(f"Product {self.name} is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise RuntimeError(
                f"Not enough {self.name} in stock. Available: {self.quantity}"
            )

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity
