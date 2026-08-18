from utils  import input_number, load_products, save_products, find_products

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

    price = input_number("Price: ")
    stock = input_number("Stock: ")

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

    quantity = input_number("Quantity: ")

    product = find_products(products, name)
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

    product = find_products(products, name)
    if product:
        products.remove(product)
        save_products(products)
        print("Product removed!")
    else:
        print("Product not found!")