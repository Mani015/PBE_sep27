# Nested dictionary: We have take another dictionary inside dict
nested_dict = {1:{'a':12,'b':123},2:{'c':123,'d':1234,'e':1234},3:123456}
print(nested_dict)
# {1: {'a': 12, 'b': 123}, 2: {'c': 123, 'd': 1234, 'e': 1234}, 3: 123456}

print(nested_dict.keys())
# dict_keys([1, 2, 3])

print(nested_dict.values())
# dict_values([{'a': 12, 'b': 123}, {'c': 123, 'd': 1234, 'e': 1234}, 123456])

print(nested_dict[1].values())
# dict_values([12, 123])

print(nested_dict[1].keys())
# dict_keys(['a', 'b'])

print(nested_dict[1].items())
# dict_items([('a', 12), ('b', 123)])

