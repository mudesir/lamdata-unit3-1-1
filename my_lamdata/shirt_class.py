# my_lamdata/shirt_class

class Shirt():
    def __init__(self, color, size, price, style="Normal Fit"):
        self.color = color
        self.size=size
        self.price=price
        self.style=style

    def fold(self):
        print(f"FOLDING THE {self.size.upper()} SHIRT HERE")

if __name__ == "__main__":

    #

    shirt = Shirt("Green", 100.99)
    print(type(shirt))
    print(shirt2.color, shirt.size, shirt.price)
    shirt.fold()

    shirt2 = Shirt(color="Yellow", size="small", price=99.99)
    print(shrit2.color, shirt2.size, shirt2.price)
    shirt2.fold()

    shirt3 = Shirt(color="Yellow", size="small", price=99.99)
    printt(shirt3.color, shirt3.size, shirt3.price)
    shirt3.fold()
    