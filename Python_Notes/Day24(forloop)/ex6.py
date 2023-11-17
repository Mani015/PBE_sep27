
name = ['gangadhar','velu','karthik','sam','ramu','raju','naga','penchalaiah','ramu','sam']

l1 = []
print('before l1:',l1)
print()
l2 = []
print('before l2:',l2)
for i in name:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)

print('After l1:',l1)
print('After l2:',l2)


# before l1: []
#
# before l2: []
# After l1: ['gangadhar', 'velu', 'karthik', 'sam', 'ramu', 'raju', 'naga', 'penchalaiah']
# After l2: ['ramu', 'sam']

