
# GLobal Keyword:
# In Python, the global keyword allows you to change a variable value outside of its current scope.
# It is used to make changes to a global variable from a local location.
# The global keyword is only required for altering the variable value and not for publishing or accessing it.


# def Fun1():
#     g1 = 10
#     print('local var:',g1)  #local var: 10
# Fun1()
# print('local var:',g1)  NameError: name 'g1' is not defined


# how to get local variable to the outside of the function


def Fun2():
    global g1
    g1 = 20
    print('local variable:',g1)
Fun2()
print('local variable:',g1)
# local variable: 20
# local variable: 20
