

from practice.utils import load_products, save_products

def get_product_by_name(product_name):
    products = load_products()

    for product in products:
        if product["name"].lower() == product_name.lower():
            return product

    return None

def get_all_products():
    return load_products()

def create_product(name, price, stock):
    products = load_products()
    for product in products:

        if product["name"].lower() == name.lower():
            return None

    new_product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(new_product)
    save_products(products)

    return new_product

def update_product(product_name, price, stock):
    products = load_products()

    for product in products:
        if product["name"].lower() == product_name.lower():
            product["price"] = price
            product["stock"] = stock

            save_products(products)
            return product
    return None

def delete_product(product_name):
    products = load_products()

    for product in products:
        if product["name"].lower() == product_name.lower():
            products.remove(product)
            save_products(products)


            return True

    return False
