
# The intersection_update() method removes the items that is not present
# in both sets (or in all sets if the comparison is done between more than two sets).
#
# The intersection_update() method is different from the intersection() method,
# because the intersection() method returns a new set, without the unwanted items,
# and the intersection_update() method removes the unwanted items from the original set.
#
# Syntax
# set.intersection_update(set1, set2 ... etc)



x1 = {'nani','ramesh','suresh','vinod','sai'}
x2 = {'sai','bharath','nithin','velu','raju','vinod'}

print('before x1:',x1)
print('before x2:',x2)

# x1.intersection_update(x2)

# print('After x1:',x1)
# print('After x2:',x2)

# before x1: {'sai', 'ramesh', 'nani', 'vinod', 'suresh'}
# before x2: {'raju', 'nithin', 'bharath', 'sai', 'vinod', 'velu'}
# After x1: {'vinod', 'sai'}
# After x2: {'raju', 'nithin', 'bharath', 'sai', 'vinod', 'velu'}


x2.intersection_update(x1)

print('After x1:',x1)
print('After x2:',x2)

# before x1: {'vinod', 'sai', 'suresh', 'ramesh', 'nani'}
# before x2: {'vinod', 'sai', 'bharath', 'velu', 'raju', 'nithin'}
# After x1: {'vinod', 'sai', 'suresh', 'ramesh', 'nani'}
# After x2: {'sai', 'vinod'}
