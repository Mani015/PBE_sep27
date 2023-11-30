
# Default Arguments in Python
# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls.
# If we provide a value to the default arguments during function calls, it overrides the default value.
# The function can have any number of default arguments.
# Default arguments should follow non-default arguments.


def Employee(name='velu',age=21,salary=40000):
    print('name:',name)
    print('age:',age)
    print('salary:',salary)
# Employee()
# name: velu
# age: 21
# salary: 40000

# How to update single parameter
# Employee('Gangadharam')

# name: Gangadharam
# age: 21
# salary: 40000

# to update a particular value
# Using Keyword Arguments

Employee(salary = 20000)
# name: velu
# age: 21
# salary: 20000
