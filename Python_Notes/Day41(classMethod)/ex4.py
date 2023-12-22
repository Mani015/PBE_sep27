
class Person:
    def __init__(self,Name,Age,Phone):
        self.name = Name
        self.age = Age
        self.phone = Phone

    # @classmethod
    # def Calling_Instancevariable_byusingclassmethod(cls):
    #     print(self.name)
    #     print(self.age)

ob1 = Person('Karthik',22,1234567)
# ob1.Calling_Instancevariable_byusingclassmethod()
# NameError: name 'self' is not defined