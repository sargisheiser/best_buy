import products
import store


def start(store_obj: store.Store):
    """
    Start the interactive CLI for the store.
    Shows menu, handles user input, and processes orders.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\nAvailable Products:")
            for idx, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{idx}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")

        elif choice == "2":
            print(f"\nTotal quantity in store: {store_obj.get_total_quantity()}")

        elif choice == "3":
            handle_order(store_obj)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def handle_order(store_obj: store.Store):
    """
    Handle user order input and place the order in the store.
    """
    shopping_list = []
    products_list = store_obj.get_all_products()

    print("\nEnter product numbers and quantities (type 'done' to finish):")
    for idx, product in enumerate(products_list, start=1):
        print(f"{idx}. {product.name} (Available: {product.quantity})")

    while True:
        selection = input("Choose product number (or 'done'): ")
        if selection.lower() == "done":
            break
        try:
            prod_index = int(selection) - 1
            if prod_index < 0 or prod_index >= len(products_list):
                print("Invalid product number. Try again.")
                continue

            qty = int(input("Enter quantity: "))
            shopping_list.append((products_list[prod_index], qty))

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    if shopping_list:
        try:
            total_cost = store_obj.order(shopping_list)
            print(f"\nOrder placed successfully! Total cost: {total_cost} dollars")
        except (ValueError, RuntimeError) as error:
            print(f"Order failed: {error}")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)