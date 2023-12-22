
# static method
# In general this methods are general utility methods inside this methods we won't use any
# Instance variable,Here won't provide self or cls arguments
# 1).Bound to the class
# 2). It can modify the class state
# 3).It can only access class variables
# 4).used to create factory methods


class Fruit(object):
    taste = 'Sweet' # class variable

    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

    def Display(self):
        print(f'name : {self.name}\n'
              f'price : {self.price}\n'
              f'color : {self.color}\n')

ob1 = Fruit('Banana',10,'yellow')
ob1.Display()
print(ob1.taste)