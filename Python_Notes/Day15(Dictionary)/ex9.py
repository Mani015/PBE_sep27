
nc1 = {'name': 'Gangadharam', 'age': 22, 'location': 'chennai', 'salary': 30000, 'phoneno': 1234567, 'rollno': 22}

# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
#
# The view object will reflect any changes done to the dictionary, see example below.
#
# Syntax
# dictionary.keys()


print(nc1.keys())

# dict_keys(['name', 'age', 'location', 'salary', 'phoneno', 'rollno'])



# syn: dict.values()
print(nc1.values())
# dict_values(['Gangadharam', 22, 'chennai', 30000, 1234567, 22])
