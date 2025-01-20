class Customer:
    def __init__(self, firstname, name, cart):
        self.firstname = firstname
        self.name = name
        self.cart = cart

    # Affiche le client et son panier
    def display_customer(self):
        print("=======================================")
        print(f"Client: {self.firstname} {self.name}")
        print(f"Date: {self.cart.date}")
        print("Panier:")
        self.cart.display_cart()
        print("=======================================")
