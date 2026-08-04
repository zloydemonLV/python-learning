import json

def load_products():
    with open("inventory.json", "r") as file:
        return json.load(file)

def save_products(products):
    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

def find_product(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product

        return None


def show_products():
    products = load_products()

    for product in products:
        print(
            f"Name: {product['name']} | "
            f"Price: {product['price']} | "
            f"Stock: {product['stock']}"
        )


def add_product():
    products = load_products()

    name = input("Product name: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))

    found = False

    for product in products:
        if product["name"].lower() == name.lower():
            found = True
            break

    if found:
        print("Product already exists!")

    else:
        new_product = {
            "name": name,
            "price": price,
            "stock": stock
        }

        products.append(new_product)

        save_products(products)
        print("Product added!")

def sell_product():
    products = load_products()

    name = input("Product name: ")
    quantity = int(input("Quantity: "))

    product = find_product(products, name)
    if product:
        if product["stock"] >= quantity:
            product["stock"] -= quantity
            save_products(products)
            print("Product sold!")

        else:
            print("Not enough stock!")
    else:
        print("Product not found!")

def remove_product():
    products = load_products()

    name = input("Product name: ")

    product = find_product(products, name)
    if product:
        product.remove(product)
        save_products(products)
        print("Product removed!")
    else:
        print("Product not found!")

while True:
    print("\n=== Inventory Manager ===")
    print("1. Show products")
    print("2. Add product")
    print("3. Sell product")
    print("4. Remove product")
    print("5. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        show_products()

    elif choice == "2":
        add_product()


    elif choice == "3":
        sell_product()


    elif choice == "4":
      remove_product()


    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")

