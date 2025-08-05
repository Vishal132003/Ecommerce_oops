class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        total = self.total_price()
        self.items.clear()
        return total
