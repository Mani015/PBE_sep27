name=input('enter a name')
print(type(name))
age=int(input('enter your  age'))
print(type(age))
details='my name is'+name+'age is'+age
print(details)
# enter a namevellu
# <class 'str'>
# enter your  age21
# <class 'int'>
# Traceback (most recent call last):
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day17(userInput)\ex-3.py", line 5, in <module>
#     details='my name is'+name+'age is'+age
# TypeError: can only concatenate str (not "int") to str
#
# Process finished with exit code 1