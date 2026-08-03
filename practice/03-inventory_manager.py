import json

while True:
    print("\n=== Inventory Manager ===")
    print("1. Show products")
    print("2. Add product")
    print("3. Sell product")
    print("4. Remove product")
    print("5. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        with open("inventory.json", "r") as file:
            products = json.load(file)

        for product in products:
            print(
                f"Name: {product['name']} | "
                f"Price: {product['price']} | "
                f"Stock: {product['stock']}"
            )



    elif choice == "2":
        with open("inventory.json", "r") as file:
            products = json.load(file)

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

            with open("inventory.json", "w") as file:
                json.dump(products, file, indent=4)

            print("Product added!")



    elif choice == "3":
        with open("inventory.json", "r") as file:
            products = json.load(file)

        name = input("Product name: ")
        quantity = int(input("Quantity: "))

        found = False

        for product in products:
            if product["name"].lower() == name.lower():
                found = True

                if product["stock"] >= quantity:
                    product["stock"] -= quantity

                    with open("inventory.json", "w") as file:
                        json.dump(products, file, indent=4)

                    print("Product sold!")

                else:
                    print("Not enough stock!")

                break

        if not found:
            print("Product not found!")



    elif choice == "4":
        with open("inventory.json", "r") as file:
            products = json.load(file)

        name = input("Product name: ")

        found = False

        for product in products:
            if product["name"].lower() == name.lower():
                products.remove(product)
                found = True
                break

        if found:
            with open("inventory.json", "w") as file:
                json.dump(products, file, indent=4)

            print("Product removed!")

        else:
            print("Product not found!")



    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")

    if choice == "3":
        with open("inventory.json", "r") as file:
            products = json.load(file)

        name = input("Product name: ")
        quantity = int(input("Quantity: "))

        for product in products:
            if product["name"] == name:
                product["stock"] -= quantity
                break
        with open("inventory.json", "w") as file:
            json.dump(products, file, indent=4)

    if choice == "4":

        with open("inventory.json", "r") as file:
            products = json.load(file)

        name = input("Product name: ")

        for product in products:
            if product["name"] == name:
                products.remove(product)
                break

        with open("inventory.json", "w") as file:
            json.dump(products, file, indent=4)

        print("Product removed!")

    if choice == "5":
        print("Exiting...")
        break
