from product import Product
from store import Store
from user import User

store = Store()
store.add_product(Product(1, "Laptop", 70000))
store.add_product(Product(2, "Mouse", 500))
store.add_product(Product(3, "Keyboard", 1000))

user = User("Vishal")
user.create_cart()

while True:
    print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        store.list_products()

    elif choice == '2':
        pid = int(input("Enter Product ID to add to cart: "))
        product = store.get_product_by_id(pid)
        if product:
            user.cart.add_to_cart(product)
            print("Added to cart.")
        else:
            print("Product not found.")

    elif choice == '3':
        user.cart.view_cart()

    elif choice == '4':
        total = user.cart.checkout()
        print(f"Checked out successfully. Total: ₹{total}")

    elif choice == '5':
        print("Thanks for visiting!")
        break

    else:
        print("Invalid Option❌.")
