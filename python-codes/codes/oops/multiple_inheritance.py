class One:
    vone = "variable two"
    def mone(self):
        print("i am one")
        print(self.vone)

class Two:
    vtwo = "variable two"
    def mtwo(self):
        print("i am two")
        print(self.vtwo)

class Three(One,Two):
    vthree = "variable three"
    def mthree(self):
        print("i am three")

    def mthreetwo(self):
        super().mone() # calling from inherited class
        super().mtwo()
        self.mthree() # calling in same class
        print(self.vthree)


# object to access all value

three = Three()
three.mthree()
three.mtwo()
three.mone()

three.mthreetwo()