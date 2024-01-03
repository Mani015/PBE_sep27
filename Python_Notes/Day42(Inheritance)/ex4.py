class Parent1:
    def Property2(self):
        print('I am Parent1 class')
class Parent2:
    def Property2(self):
        print('I am Parent2 class')
class Parent3:
    def Property3(self):
        print('I am Parent3 class')
class Child(Parent1,Parent2,Parent3):
    def Property4(self):
        print('I am child class')
ob1 = Child()
ob1.Property2()
ob1.Property3()
# ob1.Property4()
# I am Parent1 class
# I am Parent3 class
# I am child class



# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.
# --------------------------------------------------------------------------------------------------------------
# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one parent class and multiple child classes.
# -----------------------------------------------------------------------------------------------------------------------------
# Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.