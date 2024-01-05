
class Parent:
    def M1(self):
        print('I am Parent class')

class Child(Parent):
    def M1(self):
        print('I am CHild class')
        # super().M1()
ob1 = Child()
ob1.M1()