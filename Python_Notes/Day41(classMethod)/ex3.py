from datetime import date
class Student(object):
    def __init__(self,Name,Age):
        self.name = Name
        self.age = Age
        print(f'Student name : {self.name} + student age : {self.age}')

    @classmethod
    def DateofBirthYear(cls,Name,year):  # class method
        print(Name,date.today().year - year)


ob1 = Student('Velu',23)
# Student name : Velu + student age : 23
print()
ob2 = Student.DateofBirthYear('Velu',2000)

ob3 = Student.DateofBirthYear('Ramu',1999)



