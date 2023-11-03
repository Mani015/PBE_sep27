# The fromkeys() method returns a dictionary with the specified keys and the specified value.

# Syntax
# dict.fromkeys(keys, value)

num = {1,2,3,4,5,6,7,8}
type = 'int'

num_type = {}

print(num_type.fromkeys(num,type))
# {1: 'int', 2: 'int', 3: 'int', 4: 'int', 5: 'int', 6: 'int', 7: 'int', 8: 'int'}

x1 = {}.fromkeys(['gangadharam','velu','karthik','ramu'],'PFS')
print(x1)
# {'gangadharam': 'PFS', 'velu': 'PFS', 'karthik': 'PFS', 'ramu': 'PFS'}

