
# Dictionary Doesn't allows duplicate keys

x1 = {'name':'Velu','age':22,'location':'chennai','salary':30000}
print(x1)

# The update() method inserts the specified items to the dictionary.
#
# The specified items can be a dictionary, or an iterable object with key value pairs.
#
# Syntax
# dictionary.update(iterable)

x1.update({'name':'Gangadharam'})
print(x1)
# {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000}


x1.update({'phoneno':1234567})
print(x1)

# {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567}

# Dict allows duplicate values

x1.update({'rollno':22})
print(x1)
# {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567, 'rollno': 22}
