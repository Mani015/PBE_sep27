
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
#
# Syntax
# set.symmetric_difference_update(set)



s1 = {1,2,3,4,5,6,7}
s2 = {'apple','mango',1,2,3,4}
print('before set1:',s1)
print('before set2:',s2)

s1.symmetric_difference_update(s2)

print('After set1:',s1)
print('After set2:',s2)
# before set1: {1, 2, 3, 4, 5, 6, 7}
# before set2: {1, 2, 3, 4, 'apple', 'mango'}
# After set1: {5, 6, 7, 'mango', 'apple'}
# After set2: {1, 2, 3, 4, 'apple', 'mango'}


