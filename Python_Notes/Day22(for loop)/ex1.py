
x = [1,2,3]
y = x
print(y)
y[1] = 4
# print(x)
# print(y)
y[3]= 22
# print(x)

print(y)
print(id(x))

print(id(y))
print()
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))