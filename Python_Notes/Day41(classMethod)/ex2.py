# How to define class method
# by using decorator of '@classmethod', class method takes 1st parameter as  cls

class Fruit(object):
    taste = 'Sweet' # class variable

    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

    def Display(self):
        print(f'name : {self.name}\n'
              f'price : {self.price}\n'
              f'color : {self.color}')
    @classmethod
    def Update_classvariable(cls,NewTaste):
        cls.taste = NewTaste
        print(cls.taste)



ob1 = Fruit('Banana',10,'yellow')
ob1.Display()
print(ob1.taste)

print()
ob1.Display()
ob1.Update_classvariable('Sour')


# name : Banana
# price : 10
# color : yellow
# Sweet
#
# name : Banana
# price : 10
# color : yellow
# Sour
