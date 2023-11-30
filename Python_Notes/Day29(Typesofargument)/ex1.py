# Types of Arguments:In python there are four types of Arguments:

# 1)Positional Arguments in Python
# During a function call,
#values passed through arguments should be in the order of parameters in the function definition.
# This is called positional arguments.
#
# Keyword arguments should follow positional arguments only.
def func1(a,b):
    print(a,b)

# func1()
# TypeError: func1() missing 2 required positional arguments: 'a' and 'b'

# func1(10)
# ypeError: func1() missing 1 required positional argument: 'b'
# func1(10,20)
# 10 20

def fun1(x,y,z):
    print('x is:',x)
    print('y is:',y)
    print('z is:',z)

# fun1(1,2,3)
# x is: 1
# y is: 2
# z is: 3

x = 10
y = 20
z = 30

fun1(z,x,y)
# x is: 30
# y is: 10
# z is: 20



