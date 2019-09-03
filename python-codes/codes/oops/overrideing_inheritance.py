class Animal:

    def dog(self):
        print("i am a dog")

    def cat(self):
        print("i am a cat")


class Pet(Animal):
    def dog(self):
        print("wof wof")


animal = Animal()
animal.dog()

pet = Pet()
pet.dog()
pet.cat()


class Dad:
    vdad = 123

    def family(self):
        print("dad family")
        print(self.vdad)


class Son(Dad):

    def sfamily(self):
        print("my family")
        print(super().vdad)
        super().family()

son = Son()
son.sfamily()