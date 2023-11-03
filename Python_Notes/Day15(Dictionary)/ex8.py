
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list
# dict.items()

dc2 = {'chair':1000,'bed':10000,'sofa':12000,'fridge':20000}

print(dc2.items())
# dict_items([('chair', 1000), ('bed', 10000), ('sofa', 12000), ('fridge', 20000)])

print(dc2.items([2]))
# TypeError: dict.items() takes no arguments (1 given)
