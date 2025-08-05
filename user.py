class User:
    def __init__(self, username):
        self.username = username
        self.cart = None

    def create_cart(self):
        from cart import Cart
        self.cart = Cart()
