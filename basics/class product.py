class Product:
    def __init__( self, name, price, stock ):
        self.name = name
        self.price = price
        self.stock = stock
    def show_info( self ):
        print(self.name)
        print(self.price)
        print(self.stock)

cola = Product("Cola", 25, 10)
cola.show_info()
