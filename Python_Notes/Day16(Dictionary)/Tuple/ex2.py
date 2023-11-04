
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
#
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

t3 = (11,22,33,11,44,55,66,77,22)
print(t3[0])
# 11

print(t3[2])
# 33


# index: tuple.index(sub,start,stop)

print(t3.index(11,2,5))
# 3


