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



