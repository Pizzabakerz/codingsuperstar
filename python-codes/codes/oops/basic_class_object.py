class Sample:
    a = "class variable"

    def somname(self):
        print("i am a class method")

sample = Sample()
sample.somname()
print(sample.a)


# access class variable and method inside class

class Sampletwo:
    a = 123

    def one(self):
        print("one")

    def two(self):
        print(self.a) # access variable
        self.one() # access method

sample = Sampletwo()
sample.one()
print(sample.a)
sample.two()


# method with parameter and return in class

class Operation:
    def add(self,a,b):
        return a+b

op = Operation()
print(op.add(12,3))
