# constructor without parameter / default constructor

class Car:
    def __init__(self):
        self.name = "audi"
        self.price = 12345.56

    def details(self):
        print(self.name)
        print(self.price)

car = Car()
car.details()


class CarData:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def details(self):
        print(self.name)
        print(self.price)

car = CarData("honda",24356.45)
car.details()