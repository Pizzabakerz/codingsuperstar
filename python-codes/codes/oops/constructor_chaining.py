class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name)
        print(self.age)

student = Student("jack",15)
student.details()

class College(Student):

    def __init__(self,name,age,cutoff):
        self.cutoff = cutoff
        super().__init__(name,age)

    def adminssion(self):
        print(self.name)
        print(self.age)
        print(self.cutoff)

college = College("sam",12,123)
college.adminssion()