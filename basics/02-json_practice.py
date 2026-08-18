import json

products = [
    {"name": "Jack Daniel's", "price": 30, "stock": 5},
    {"name": "Glenfiddich", "price": 60, "stock": 2},
    {"name": "Red Label", "price": 22, "stock": 15}
]
with open("../practice/inventory.json", "w") as file:
    json.dump(products, file, indent=4)

with open("../practice/inventory.json", "r") as file:
    products = json.load(file)
print(products)
products.append({"name": "Chivas Regal", "price": 45, "stock": 7})
with open("../practice/inventory.json", "w") as file:
    json.dump(products, file, indent=4)
print(products)
with open("../practice/inventory.json", "r") as file:
    products = json.load(file)

for product in products:
    if product["name"] == "Chivas Regal":
        products.remove(product)
        break

with open("../practice/inventory.json", "w") as file:
    json.dump(products, file, indent=4)

print(products)
