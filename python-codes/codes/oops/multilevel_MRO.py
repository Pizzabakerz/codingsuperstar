class One:
    vone = "variable two"
    def mone(self):
        print("i am one")
        print(self.vone)

class Two(One):
    vtwo = "variable two"
    def mtwo(self):
        print("i am two")
        print(self.vtwo)

class Three(Two):
    vthree = "variable three"
    def mthree(self):
        print("i am three")
        print(self.vthree)


class Four:
    vfour = "variable four"
    def mfour(self):
        print("i am four")
        print(self.vfour)

class Five(Three,Four):
    vfive = "variable five"
    def mfive(self):
        print("i am five")

    def accessall(self):
        # from class one
        super().mone()
        print(super().vone)

        # from class two
        super().mtwo()
        print(super().vtwo)

        # from class three
        super().mthree()
        print(super().vthree)

        # from class four
        super().mfour()
        print(super().vfour)

five = Five()
five.mone()
five.mtwo()
five.mthree()
five.mfour()
five.mfive()
five.accessall()




