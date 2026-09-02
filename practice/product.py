class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        if not isinstance(value, int):
            raise TypeError("Stock must be an integer")

        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value


    def show_info(self):
        print(f"Name: {self.name} | Price: {self.price} | Stock: {self.stock}")

    def sell(self , quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if self.stock >= quantity:
            self.stock -= quantity
            print( "Product Sold")
            return True
        else:
            print("Not enough stock")
            return False

    def add_stock(self, quantity):
        self.stock += quantity


