class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        print(f"Name: {self.name} | Price: {self.price} | Stock: {self.stock}")

    def sell(self , quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print( "Product Sold")
            return True
        else:
            print("Not enough stock")
            return False

    def add_stock(self, quantity):
        self.stock += quantity

