
# The difference_update() method removes the items that exist in both sets.
#
# The difference_update() method is different from the difference() method,
# because the difference() method returns a new set, without the unwanted items,
# and the difference_update() method removes the unwanted items from the original set.
#
# Syntax
# set.difference_update(set)

s1 = {1,2,3,4,5,6}
print('before set1:',s1)
s2 = {1,4,7,8,9,0}
print('before set2:',s2)
# before set1: {1, 2, 3, 4, 5, 6}
# before set2: {0, 1, 4, 7, 8, 9}

s1.difference_update(s2)

print('After set1:',s1)
print('After set2:',s2)
# After set1: {2, 3, 5, 6}
# After set2: {0, 1, 4, 7, 8, 9}