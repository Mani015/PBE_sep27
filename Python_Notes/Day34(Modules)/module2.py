
# How to import modules?
# In Python, the import statement is used to import the whole module.
# Also, we can import specific classes and functions from a module.

# 1st method


import module1

print('Addition:',module1.var1 + module1.var2)
# Addition: 30


def New(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    var = [add,sub,mul,div]
    return var


