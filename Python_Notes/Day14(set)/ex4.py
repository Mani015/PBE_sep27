
# The isdisjoint() method returns True if none of the items are present in both sets,
# otherwise it returns False.
#
# Syntax
# set.isdisjoint(set)

a1 = {1,2,3,4,5,6}
a2 = {6,7,8,9,10}

# if none of the items are present in both sets,otherwise it returns False.
print(a1.isdisjoint(a2))
# False

# returns True if none of the items are present in both sets
a3 = {11,22,33}
print(a3.isdisjoint(a1))
# True
