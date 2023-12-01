
# Understanding Scope
# In programming, the scope of a name defines the area of a program in which you can unambiguously access that name,
#  such as variables, functions, objects, and so on. A name will only be visible to and accessible by the code in its scope.
#  Several programming languages take advantage of scope for avoiding name collisions and unpredictable behaviors.

# 1).Global Scope
# 2).Local Scope
# 3). Enclosing/Non-local Scope
# 4).Built-in Scope


# 1).Global Scope:
# How to define global variable:

# global variable: A variable is defined outside of the fucntion , then is called global variable
# global variable is a variable , that variable declared outside of the function is called global varaible

# x1 = 10
# print('Global variable:',x1)
# def Fun():
#     print('Local scope')
# Fun()
# Global variable: 10
# Local scope



# global variable using local scope & outside of the function
x2 = 20
print('global var:',x2)

def Fun1():
    print('global var:', x2)

Fun1()
print('global var:',x2)


# Global scope: The names that you define in this scope are available to all your code.