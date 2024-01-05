# Polymorphism
# one person can do a multiple tasks

# ex : +,*,print(),type(), max(), min(), sum()

# Polymorphism in Python is the ability of an object to take many forms.
# In simple words, polymorphism allows us to perform the same action in many different ways.
#
# For example, Jessa acts as an employee when she is at the office. However, when she is at home,
# she acts like a wife. Also, she represents herself differently in different places.
#  Therefore, the same person takes different forms as per the situation.


# Polymorphism With Inheritance
# Polymorphism is mainly used with inheritance.
# In inheritance, child class inherits the attributes and methods of a parent class.
# The existing class is called a base class or parent class,
# and the new class is called a subclass or child class or derived class.


# Using method overriding polymorphism allows us to defines methods
# in the child class that have the same name as the methods in the parent class.
# This process of re-implementing the inherited method in the child class is known as Method Overriding.

class Human1:
    def __init__(self,Name,Age,Salary):
        self.name = Name
        self.Age = Age
        self.Salary = Salary

class Human1:
    def __init__(self,Name,Age,Salary):
        self.name = Name
        self.Age = Age
        self.Salary = Salary

        print(self.name,self.Age,self.Salary)


# ob1 = Human1('Velu',23,30000)
# TypeError: __init__() missing 1 required positional argument: 'Location'


ob2 = Human1('Gangadharam',23,40000,)

# Gangadharam 23 40000