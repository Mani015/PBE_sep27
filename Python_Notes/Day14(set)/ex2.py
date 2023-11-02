s1 = {1,2,3,4,5,6}
print('before set1:',s1)
s2 = {1,4,7,8,9,0}
print('before set2:',s2)
# before set1: {1, 2, 3, 4, 5, 6}
# before set2: {0, 1, 4, 7, 8, 9}

s2.difference_update(s1)

print('After set1:',s1)
print('After set2:',s2)
# After set1: {1, 2, 3, 4, 5, 6}
# After set2: {0, 7, 8, 9}
