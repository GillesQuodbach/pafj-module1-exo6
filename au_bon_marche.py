from cart import Cart
from customer import Customer
from product import stock_dictionary

is_shopping_over = False
is_computer_off = False
is_new_product = False

all_carts_list = []
all_customer_list = []


# affichage du stock
def display_stock():
    for product_name, product_values in stock_dictionary.items():
        print(f"{product_name}: stck={product_values.quantity}, px={product_values.price}€/{product_values.part_or_kg}")


display_stock()


print("Bienvenue au bon marché")

while not is_computer_off:
    user_input = input("Afficher le bilan de la journée (1) / Faire vos courses (2) / Quitter (3) \n")

    if user_input == "1":
        print("Bilan client de la journée")
        for customer in all_customer_list:
            customer.display_customer()
        print("===============================")
        print("Stock actuel")
        display_stock()
        print("===============================")
    elif user_input == "2":
        while not is_shopping_over:
            user_firstname = input("Veuillez entrer votre prénom\n")
            user_name = input("Veuillez entrer votre nom\n")

            cart = Cart()
            customer = Customer(user_firstname, user_name, cart)

            while not is_new_product:
                user_product_name = input("Veuillez choisir un article / stop pour terminée vos achats").capitalize()
                if user_product_name == "Stop":
                    is_new_product = True
                    is_shopping_over = True
                    all_carts_list.append(cart)
                    all_customer_list.append(customer)
                    customer.display_customer()
                else:
                    user_product_quantity = int(input("Entrez la quantité"))
                    cart.add_item(user_product_name, user_product_quantity)
                    cart.display_cart()
                    display_stock()

    elif user_input == "3":

        print("Au revoir")
        is_computer_off = True
