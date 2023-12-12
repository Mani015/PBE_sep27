# swapping using two variables:

a = 12
b = 13
print('before a:',a)
print('before b:',b)

a = a + b
# 12 + 13 = 25
b = a - b
# b = 25 - 13 = 12
a = a - b
# a = 25 - 12

print('After a:',a)
print('After b:',b)

print(a/b)
# before a: 12
# before b: 13
# After a: 13
# After b: 12

# 1.0833333333333333




x,y = 2,3
x, y = y, x
