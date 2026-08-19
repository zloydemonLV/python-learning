import json

def input_number(message, min_value=0, max_value=1000000):
    while True:
        try:
            number = int(input(message))

            if number < min_value or number > max_value:
                print("Number is out of range!")
                continue

            return number

        except ValueError:
            print("Number must be a number!")

def load_products():
    with open("inventory.json", "r") as file:
        return json.load(file)

def save_products(products):
    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

def find_products(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product

    return None