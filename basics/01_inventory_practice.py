products = [
    {"name": "Jameson", "price": 25, "stock": 12},
    {"name": "Jack Daniel's", "price": 30, "stock": 5},
    {"name": "Glenfiddich", "price": 60, "stock": 2},
    {"name": "Red Label", "price": 22, "stock": 15},
]
def low_stock(products):
    for product in products:
        if product["stock"] < 10:
            print(product["name"])
low_stock(products)
def total_stock(products):
    total = 0
    for product in products:
        total += product["stock"]
    return total
result = total_stock(products)
print(result)
def total_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total
result = total_value(products)
print(result)
def find_product(products,name):
    for product in products:
        if product["name"] == name:
            return product
result = find_product(products , "Jameson")
print(result)
def add_product(products,name, price, stock):
    products.append({"name": name, "price": price, "stock": stock})
add_product(products, "Ballantine's", 28, 9)
# print(products)
def update_stock(products, name, new_stock):
    for product in products:
        if product["name"] == name:
            product["stock"] = new_stock
update_stock(products, "Jameson", 20)
print(products)
def sell_product(products, name, quantity):
    for product in products:
        if product["name"] == name:
            if product["stock"] >= quantity:
                product["stock"] -= quantity
            else:
                print("Not enough stock")
sell_product(products, "Jameson", 3)
print(products)
def remove_product(products, name):
    for product in products:
        if product["name"] == name:
            products.remove(product)
remove_product(products, "Jameson")
print(products)
def most_expensive_product(products):
    most_expensive = products[0]

    for product in products:
            if product["price"] > most_expensive["price"]:
                most_expensive = product
    return most_expensive
result = most_expensive_product(products)
print(result)
def cheapest_product(products):
    cheapest = products[0]

    for product in products:
        if product["price"] < cheapest["price"]:
            cheapest = product

        return cheapest

result = cheapest_product(products)
print(result)
def sort_by_price(products):
    sorted_products = sorted(products, key=lambda product: product["price"])
    return sorted_products

result = sort_by_price(products)
print(result)
def sort_by_stock(products):
    sorted_products = sorted(products, key=lambda product: product["stock"])
    return sorted_products
result = sort_by_stock(products)
print(result)

def save_products(products):
    with open("../practice/inventory.txt", "w") as file:
        for product in products:
            file.write(
                product["name"] + ";" +
                str(product["price"]) + ";" +
                str(product["stock"]) + "\n"
            )
save_products(products)

def load_products():
    products = []

    with open("../practice/inventory.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            name, price, stock = line.split(";")

            product = {
                "name": name,
                "price": int(price),
                "stock": int(stock)
            }

            products.append(product)

    return products
products = load_products()
print(products)












