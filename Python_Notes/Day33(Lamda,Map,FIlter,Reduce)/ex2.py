
# Do if else using lambda

# print((lambda var : 'even' if var%2==0 else 'Odd')(var = int(input('Enter a number:'))))
# Enter a number:6
# even


# The map(), filter() and reduce() functions bring a bit of functional programming to Python.

# All three of these are convenience functions that can be replaced with List Comprehensions or loops,
# but provide a more elegant and short-hand approach to some problems.
#
# The map() Function
# The map() function iterates through all items in the given iterable and executes
# the function we passed as an argument on each of them.

# iterable ---> list,tuple,set,string


# syn: map(function_name,iterable/sequence)


def New(var):
    return var**2

l1 = [1,2,3,4,5,6,7,8,9,10]

x1 = map(New,l1)
# print(x1)
# <map object at 0x0000028B9CA89BE0>
# print(type(x1))
# <class 'map'>

print(list(x1))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print()
l2 = [3,4,6,4,2,4,6,7,8]

x2 = map(New,l2)
print(tuple(x2))
# (9, 16, 36, 16, 4, 16, 36, 49, 64)