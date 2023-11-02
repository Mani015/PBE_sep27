
# Python frozenset()
# Frozen set is just an immutable version of a Python set object.
# While elements of a set can be modified at any time,
# elements of the frozen set remain the same after creation.
#
# Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.

s1 = {1,2,3,4}
print(type(s1))

s2 = frozenset(s1)
print(type(s2))
# <class 'frozenset'>


l1 = [1,2,3,4,5,6,7]

l2 = frozenset(l1)
print(l2)
# frozenset({1, 2, 3, 4, 5, 6, 7})
