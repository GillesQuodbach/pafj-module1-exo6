
class Product:
    def __init__(self, name, price, quantity, part_or_kg):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.part_or_kg = part_or_kg


stock_list = [
    Product("Clémentine", 2.90, 6, "kg"),
    Product("Carotte", 1.30, 7, "kg"),
    Product("Datte", 7.00, 4, "kg"),
    Product("Choux de Bruxelles", 4.00, 4, "kg"),
    Product("Grenade", 3.50, 3, "kg"),
    Product("Chou vert", 2.50, 12, "pièce"),
    Product("Kaki", 4.50, 3, "kg"),
    Product("Courge butternut", 2.50, 6, "pièce"),
    Product("Kiwi", 3.50, 5, "kg"),
    Product("Endive", 2.50, 5, "kg"),
    Product("Mandarine", 2.80, 6, "kg"),
    Product("Épinard", 2.60, 4, "kg"),
    Product("Orange", 1.50, 8, "kg"),
    Product("Poireau", 1.20, 5, "kg"),
    Product("Pamplemousse", 2.00, 8, "pièce"),
    Product("Potiron", 2.50, 6, "pièce"),
    Product("Poire", 2.50, 5, "kg"),
    Product("Radis noir", 5.00, 10, "pièce"),
    Product("Pomme", 1.50, 8, "kg"),
    Product("Salsifis", 2.50, 3, "kg"),
]

stock_dictionary = {}

for product in stock_list:
    stock_dictionary[product.name] = product
