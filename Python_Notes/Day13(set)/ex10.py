# The difference() method returns a set that contains the difference between two sets.

# syntax:-set.difference(set)

fruits={'apple','dragon','jackfruits'}
print(fruits)
fruits1={'apple','banana','mango'}
print(fruits1)
n=fruits.difference(fruits1)
print(n)
# {'dragon', 'jackfruits'}
print(fruits1.difference(fruits))
# {'banana', 'mango'}