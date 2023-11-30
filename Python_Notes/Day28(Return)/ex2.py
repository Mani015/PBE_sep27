
def Add_numbers(a,b,c):

    return a,b,c


var = Add_numbers(6,7,10)
# print(var)
# print(type(var))
# (6, 7, 10)
# <class 'tuple'>

# If i want only single value, outside of the function

def Fun1(a,b,c):
    A = a
    B = b
    C = c
    return A
var1 = Fun1(1,2,3)
# print(var1)

# We have to create another variable name , to get multiple value , with single variables
def Fun1(a,b,c):
    A = a
    B = b
    C = c
    return A,B
var2,var3 = Fun1('raju','gangadhar','velu')
print(var2)
print(var3)

# raju
# gangadhar
