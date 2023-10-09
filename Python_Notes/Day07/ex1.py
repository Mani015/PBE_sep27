
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

# is , is not
# is 	Returns True if both variables are the same object	x is y

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
# syn: x is y

print(x is y)
# False

z = x
print(z)
# [1, 2, 3, 4, 5, 6]
print(z is x)
# True

print(y is z)
# False

