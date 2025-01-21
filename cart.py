import datetime
from product import stock_dictionary


class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = {}
        else:
            self.items = items
        self.date = datetime.datetime.now()

    # Ajout d'un produit au panier
    def add_item(self, product_name: str, quantity: int):
        # Vérifie si l'objet Product est déjà dans le panier
        self.items[product_name] = quantity
        stock_dictionary[product_name].quantity -= quantity

    # Affiche le panier
    def display_cart(self):
        cart_total_price = 0
        for name, quantity in self.items.items():
            price = stock_dictionary[name].price
            total_price = price * quantity
            cart_total_price += total_price
            print(f"{name}, {quantity}, prix: {total_price}€")
        print(f"Montant total du panier: {cart_total_price}€")

