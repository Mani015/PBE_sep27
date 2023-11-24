
# Functions: A fucntion is a block of code, which only runs , when it is called
# They are two types:
# 1).Pre_defined functions/Inbuilt:
# 2).User defined functions

# 1. Built-in functions: These are standard functions in Python that are available to use.
# Some examples include len(), str(), int(), abs(), sum(), and more 1
l1 = [1,2,3,4]
print(l1)
print(max(l1))
print(min(l1))
print(len(l1))
print(sum(l1))

# 2.User-defined functions: We can create our own functions based on our requirements.
# A function is a block of code that performs a specific task. For instance,
# we can create a program to create a circle and color it.
# We can create two functions to solve this problem: create_circle() and color_circle().
# Dividing a complex problem into smaller chunks makes our program easy to understand and reuse 1.


a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
c = 12
d = 13
print(c + d)
print(c - d)
print(c * d)

# How to define a fucntion , by using def keyword
# And also given a one user function name

# fucntion name()
# sy: def function_name():
#     pass
# fucntion calling
# function_name()


# ex1:

def Task1():
    print('welcome to fucntions')

Task1()
print(type(Task1))
# welcome to fucntions
# <class 'function'>




