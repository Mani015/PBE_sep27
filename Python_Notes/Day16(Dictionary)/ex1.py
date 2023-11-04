

# How to update the value

d1 = {'a':123,'b':1234,'c':12345,'d':123456,'e':1234567}
print(d1)
# {'a': 123, 'b': 1234, 'c': 12345, 'd': 123456, 'e': 1234567}

print(d1['a'])
# 123

# syn: dict[key] = 'New_Value'

d1['b'] = 1122
print(d1)
# {'a': 123, 'b': 1122, 'c': 12345, 'd': 123456, 'e': 1234567}

d1['e'] = 11223344
print(d1)
# {'a': 123, 'b': 1122, 'c': 12345, 'd': 123456, 'e': 11223344}
