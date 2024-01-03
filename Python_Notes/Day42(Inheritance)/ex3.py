
# Multiple Inheritance
#
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.

class Parent1:
    def Property1(self):
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
ob1.Property1()
ob1.Property2()
ob1.Property3()
ob1.Property4()

# I am Parent1 class
# I am Parent2 class
# I am Parent3 class
# I am child class

