

#  Multilevel inheritance
#  In multilevel inheritance, a class inherits from a child class or derived class.
#  Suppose three classes A, B, C. A is the superclass,
#  B is the child class of A, C is the child class of B.
#  In other words, we can say a chain of classes is called multilevel inheritance.

# Grandfather---> Father ---> child
class GrandFather:
    def M1(self):
        print('I am GrandParent')

class Parent(GrandFather):
    def M2(self):
        print('I am Parent class')

class Child(Parent):
    def M3(self):
        print('I am Child class')

ob1 = Child()
ob1.M1()
ob1.M2()
ob1.M3()
# I am GrandParent
# I am Parent class
# I am Child class
