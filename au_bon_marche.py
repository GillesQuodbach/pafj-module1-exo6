from typing import List

from cart import Cart
from customer import Customer
from product import stock_dictionary

# Variables de contrôle pour gérer l'état du programme
is_shopping_over: bool = False    # Indique si les courses sont terminées
is_computer_off: bool = False     # Indique si l'application doit être fermée
is_new_product: bool = False      # Indique si un nouveau produit doit être ajouté

# Listes pour stocker les paniers et les clients
all_carts_list: List[Cart] = []
all_customer_list: List[Customer] = []


# Fonction pour afficher le stock de produits disponible
def display_stock():
    """
    Affiche la liste des produits disponibles en stock avec leurs quantités et prix.
    """
    for product_name, product_values in stock_dictionary.items():
        print(f"{product_name}: stock={product_values.quantity}, "
              f"prix={product_values.price}€/{product_values.part_or_kg}")


# Fonction pour vérifier si un produit existe dans le dictionnaire
def is_product_exist(product_name: str):
    """
    Vérifie si un produit existe dans le stock.
    :param product_name: Nom du produit à vérifier
    :return: True si le produit existe, sinon False
    """
    return product_name in stock_dictionary


# Fonction pour vérifier si la quantité demandée est disponible
def is_quantity_enough(product_name: str, user_quantity: int):
    """
    Vérifie si la quantité demandée est disponible dans le stock.
    :param product_name: Nom du produit
    :param user_quantity: Quantité demandée par l'utilisateur
    :return: True si la quantité est suffisante, sinon False
    """
    return stock_dictionary[product_name].quantity >= user_quantity


display_stock()

print("Bienvenue au bon marché")

while not is_computer_off:
    user_input: str = input("Afficher le bilan de la journée (1) / Faire vos courses (2) / Quitter (3) \n")

    if user_input == "1":
        print("Bilan clients de la journée")
        for customer in all_customer_list:
            customer.display_customer()
        print("===============================")
        print("Stock actuel")
        display_stock()
        print("===============================")
    elif user_input == "2":
        while not is_shopping_over:
            user_firstname: str = input("Veuillez entrer votre prénom\n")
            user_name: str = input("Veuillez entrer votre nom\n")

            cart: Cart = Cart()
            customer: Customer = Customer(user_firstname, user_name, cart)

            while not is_new_product:
                user_product_name: str = input("Veuillez choisir un article / stop pour terminée vos achats\n").capitalize()

                if user_product_name == "Stop":
                    is_new_product = True
                    is_shopping_over = True
                    all_carts_list.append(cart)
                    all_customer_list.append(customer)
                    customer.display_customer()
                    break

                if not is_product_exist(user_product_name):
                    print("Votre produit n'existe pas, merci de recommencer")

                else:
                    print(f"Quantité de {stock_dictionary[user_product_name].name} "
                          f"en stock: {stock_dictionary[user_product_name].quantity}/"
                          f"{stock_dictionary[user_product_name].part_or_kg}")

                    while True:
                        user_product_quantity: str = input("Entrez la quantité souhaitée:")
                        if user_product_quantity.isdigit():
                            user_product_quantity: int = int(user_product_quantity)
                            if is_quantity_enough(user_product_name, user_product_quantity):
                                cart.add_item(user_product_name, user_product_quantity)
                                cart.display_cart()
                                display_stock()
                                break
                            else:
                                print("Nous n'avons pas assez de stock ou saisie incorrect, merci d'ajuster")
                        else:
                            print("Veuillez entrer un nombre valide")

    elif user_input == "3":
        print("Au revoir")
        is_computer_off = True
