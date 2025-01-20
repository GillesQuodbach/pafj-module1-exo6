
class Product:
    def __init__(self, name, price, quantity, part_or_kg):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.part_or_kg = part_or_kg


# Constantes
KG = "kg"
PIECE = "pièce"

# Liste des produits
stock_list = [
    Product("Clémentine", 2.90, 6, KG),
    Product("Carotte", 1.30, 7, KG),
    Product("Datte", 7.00, 4, KG),
    Product("Choux de Bruxelles", 4.00, 4, KG),
    Product("Grenade", 3.50, 3, KG),
    Product("Chou vert", 2.50, 12, PIECE),
    Product("Kaki", 4.50, 3, KG),
    Product("Courge butternut", 2.50, 6, PIECE),
    Product("Kiwi", 3.50, 5, KG),
    Product("Endive", 2.50, 5, KG),
    Product("Mandarine", 2.80, 6, KG),
    Product("Épinard", 2.60, 4, KG),
    Product("Orange", 1.50, 8, KG),
    Product("Poireau", 1.20, 5, KG),
    Product("Pamplemousse", 2.00, 8, PIECE),
    Product("Potiron", 2.50, 6, PIECE),
    Product("Poire", 2.50, 5, KG),
    Product("Radis noir", 5.00, 10, PIECE),
    Product("Pomme", 1.50, 8, KG),
    Product("Salsifis", 2.50, 3, KG),
]

# Transformation de la liste des produits en dictionnaire
stock_dictionary = {}

for product in stock_list:
    stock_dictionary[product.name] = product
