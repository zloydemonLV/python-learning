
from inventory import show_products, add_product, sell_product, remove_product
from practice.utils import input_number

def main():
    while True:
        print("\n=== Inventory Manager ===")
        print("1. Show products")
        print("2. Add product")
        print("3. Sell product")
        print("4. Remove product")
        print("5. Exit")

        choice = input_number("Choose an option: ")


        if choice == 1:
            show_products()

        elif choice == 2:
            add_product()


        elif choice == 3:
            sell_product()


        elif choice == 4:
          remove_product()


        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()