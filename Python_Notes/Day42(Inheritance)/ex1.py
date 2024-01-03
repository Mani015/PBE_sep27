# The process of inheriting the properties of the parent class into a child class is called inheritance.
# The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
#
# In Object-oriented programming, inheritance is an important aspect.
# The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating
#  it from scratch.

class Parent:
    def Method1(self):
        print('I am a parent class')

class Child:
    def method2(self):
        print('I am Child class')

ob1 = Parent()
ob1.Method1()
# I am a parent class

ob2 = Child()
ob2.method2()