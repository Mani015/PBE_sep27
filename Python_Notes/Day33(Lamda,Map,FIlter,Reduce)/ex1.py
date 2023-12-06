
# Lambda is a keyword
# Lamda reduces the lines of code
# Lambda function is a small anonymous function
# A lambda function can take any number of arguments at a time
# They don't have a name

a = 10
b = 20
# print(a+b)
# 30

# sy: lambda  arguments : expression

x = lambda a,b : a + b
# print(type(x))
# <class 'function'>

# print(x)
# <function <lambda> at 0x0000019201A8DDC0>
# print(x(2,3))
# 5


print((lambda a,b : a + b)(4,5))
# 9



