
# swapping using 3rd variable name:

fname = 'Python'
lname = ' Developer'
print('Before Fname is', fname)
print('Before Lname is', lname)
print(fname + lname)
print()

# We have to take temparary variable name
temp  =  fname
fname = lname
lname = temp

print('Before Fname is', fname)
print('Before Lname is', temp)
print(fname + temp)

# Before Fname is  Developer
# Before Lname is Python
#  DeveloperPython


