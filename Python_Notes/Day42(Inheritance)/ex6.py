class GrandFather:
    def M2(self):
        print('I am GrandParent')


class Parent(GrandFather):
    def M2(self):
        print('I am Parent class')



class Child(Parent):
    def M3(self):
        print('I am Child class')


ob1 = Child()
ob1.M3()
# I am Child class
ob1.M2()
ob1.M2()
# I am Child class
# I am Parent class