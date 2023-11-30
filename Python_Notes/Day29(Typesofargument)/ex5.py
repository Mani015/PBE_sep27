
# What Are Variable-Length Arguments in Python?
# Variable-length arguments are also known as arbitrary arguments.
# If we don’t know the number of arguments needed for the function in advance,
# we can use arbitrary arguments  it defined '*'
#
# THERE ARE TWO TYPES OF ARBITRARY ARGUMENTS:
# Arbitrary positional arguments.
# Arbitrary keyword arguments.

# a).Arbitrary positional Arguments

# def fun1(a,b,c,d,e,f,g,h,i,j):
#     l1 = [a,b,c,d,e,f,g,h,i,j]
#     print('sumof:',sum(l1))
#
# fun1(1,2,3,4,5,6,7,8,9,10)
# sumof: 55





def Number(*var):
    print(var)

# Number(1,2,3,4,5,6,76,8,9,10)

# (1, 2, 3, 4, 5, 6, 76, 8, 9, 10)
def Sum_numbers(*var):
    sum = 0
    for i in var:
        sum = sum + i
    print('sum of numbers:',sum)

Sum_numbers(1,2,3,4,5,)
# sum of numbers: 15
Sum_numbers(12,13)
# sum of numbers: 25
