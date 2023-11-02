
# The issubset() method returns True if all items in the set exists in the specified set,
# otherwise it returns False.
#
# Syntax
# set.issubset(set)

a1 = {1,2,3,4,5,6}
a2 = {6,7,8,9,10}
# if all items in the set exists in the specified set,otherwise it returns False.
print(a1.issubset(a2))
# False

# True if all items in the set exists in the specified set
a3 = {6,7,8,9,10,11,22,33}

print(a2.issubset(a3))