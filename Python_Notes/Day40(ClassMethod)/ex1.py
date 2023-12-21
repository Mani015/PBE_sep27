
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

class Student(object):
    Schoolname = 'New Horizon'  # class variable
    def __init__(self,sname,sage,smarks,slocation):
        self.name = sname
        self.age = sage
        self.marks = smarks
        self.location = slocation

    def Display(self):
        print(
            self.name,self.age,self.marks,self.location
        )

s1 = Student('velu',22,100,'banglore')
s1.Display()
print(s1.Schoolname)
# New Horizon

s2 = Student('ramu',23,100,'chennai')
s2.Display()
print(s2.Schoolname)


# ramu 23 100 chennai
# New Horizon
