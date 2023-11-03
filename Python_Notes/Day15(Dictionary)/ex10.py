
# The pop() method removes the specified item from the dictionary.
#
# The value of the removed item is the return value of the pop() method, see example below.
#
# Syntax
# dictionary.pop(keyname, defaultvalue)

nc1 = {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567, 'rollno': 22}

print('before:',nc1)
nc1.pop('name')
print('After:',nc1)

# before: {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567, 'rollno': 22}
# After: {'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567, 'rollno': 22}

nc1.pop('phoneno')
print(nc1)
# {'age': 22, 'location': 'chennai', 'salary': 30000, 'rollno': 22}
