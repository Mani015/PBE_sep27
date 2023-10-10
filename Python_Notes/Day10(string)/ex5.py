
# The find() method finds the first occurrence of the specified value.
#
# The find() method returns -1 if the value is not found.
#
# The find() method is almost the same as the index() method,
# the only difference is that the index() method raises an exception if the value is not found. (See example below)


s2 = 'Namma Metro'
# syn: string.find(value,start,end)

# print(s2.find('x'))
# -1
print(s2.find('N',2,10))
# -1
print(s2.find('M'))
# 6
print(s2.find('Na'))
# 0
print(s2.find('tro',3,8))
# 8


print(s2.find('tro',3,8))
# -1

# print(s2.index('hello'))
# ValueError: substring not found
print(s2.find('hello'))