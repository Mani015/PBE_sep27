
# Keyword Arguments in Python
# Functions can also be called using keyword arguments of the form kwarg=value.
#
# During a function call,
# values passed through arguments don’t need to be in the order of
# parameters in the function definition.
# This can be achieved by keyword arguments.
# But all the keyword arguments should match the parameters in the function definition.


def Student(name,age,location):
    print('student name:',name)
    print('student age:',age)
    print('student location:',location)

# Student(name='Ramu',age=20,location='kadapa')
# student name: Ramu
# student age: 20
# student location: kadapa



# During a function call,
# values passed through arguments don’t need to be in the order of
# parameters in the function definition.





Student(age= 21,location='tirupati',name='Karthik')
# student name: Karthik
# student age: 21
# student location: tirupati
