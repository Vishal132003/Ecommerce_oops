from product import Product

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]

    def list_products(self):
        for product in self.products:
            print(product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
