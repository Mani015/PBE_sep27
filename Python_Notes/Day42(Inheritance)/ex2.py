#Single Inheritance
# In single inheritance, a child class inherits from a single-parent class.
# Here is one child class and one parent class.
class Parent:
    def Method1(self):
        print('I am a parent class')

class Child(Parent):
    def method2(self):
        print('I am Child class')


ob1 = Child()
ob1.method2()
ob1.Method1()
# I am Child class
# I am a parent class

