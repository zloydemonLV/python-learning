products = [
    {"name": "Jameson", "price": 25, "stock": 10},
    {"name": "Jack Daniel's", "price": 30, "stock": 5},
    {"name": "Glenfiddich", "price": 45, "stock": 2},
]
for product in products:
    print("===Product===")
    for key, value in product.items():
        print(f" {key} : {value}")
    print()
