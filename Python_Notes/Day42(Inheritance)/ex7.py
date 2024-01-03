# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.


class Parent:
    def Property(self):
        print('I am Parent class,My Attributes & properties belongs to my child')

class Child1(Parent):
    def Method1(self):
        print('I am Child1 class')
class Child2(Parent):
    def Method2(self):
        print('I am Child2 class')

ob1 = Child1()
ob1.Property()
ob1.Method1()
print()
ob2 = Child2()
ob2.Method2()
ob2.Property()

# I am Parent class,My Attributes & properties belongs to my child
# I am Child1 class
#
# I am Child2 class
# I am Parent class,My Attributes & properties belongs to my child
