

class Parent1:
    def m1(self):
        print('I am Parent1 class')


class Parent2(Parent1):
    def m1(self):
        print('I am Parent2 class')

class Child(Parent2):
    def m1(self):
        print(' I am Child class')
        super().m1()
        Parent1.m1(self)



ob1 = Child()
ob1.m1()
