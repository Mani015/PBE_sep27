
# The issuperset() method returns True if all items in the specified set exists in the original set,
# otherwise it returns False.
#
# Syntax
# set.issuperset(set)

s1 = {1,2,3,4,5}
s2 = {1,3,5,6,7,98,0}
print(s1.issuperset(s2))
# False

s3 = {1,2,3,4,5,6,7,8,9,10}
print(s3.issuperset(s1))
# True
