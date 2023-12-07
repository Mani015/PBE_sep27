
# The reduce() Function
# reduce() works differently than map() and filter().
# It does not return a new list based on the function and iterable we've passed.
# Instead, it returns a single value.
#
# Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
#
# The syntax is:
#
# reduce(function, sequence[, initial])
# reduce() works by calling the function we passed for the first two items in the sequence. The result returned by the function is used in another call to function alongside with the next (third in this case), element.
#
# This process repeats until we've gone through all the elements in the sequence.
#
# The optional argument initial is used, when present, at the beginning of this "loop" with the first element in the first call to function. In a way, the initial element is the 0th element, before the first one, when provided.
# from functools import reduce


from  functools import reduce
def Com(num1,num2):
    return num1 + num2


x1 = reduce(Com,[1,2,3,4,5,6,7,8,9,10])
print(x1)