import datetime
from product import stock_dictionary


class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = {}
        else:
            self.items = items
        self.date = datetime.datetime.now()

    def add_item(self, product_name, quantity):
        # Vérifie si l'objet Product est déjà dans le panier
        self.items[product_name] = quantity
        stock_dictionary[product_name].quantity -= quantity

    def display_cart(self):
        for name, quantity in self.items.items():
            price = stock_dictionary[name].price
            total_price = price * quantity
            print(f"{name}, {quantity}, prix: {total_price}€")
            # print(product_data)
