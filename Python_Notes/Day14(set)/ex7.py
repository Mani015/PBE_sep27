
# The symmetric_difference() method returns a set that contains all items from both set,
# but not the items that are present in both sets.
#
# Meaning: The returned set contains a mix of items that are not present in both sets.
#
# Syntax
# set.symmetric_difference(set)



y1 = {11,22,33,44,55,66}
y2 = {11,22,4,2,55,6}

print(y1.symmetric_difference(y2))
# {33, 2, 66, 4, 6, 44}

print(y2.symmetric_difference(y1))
# {66, 2, 4, 6, 33, 44}

