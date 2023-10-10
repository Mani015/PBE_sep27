
# The capitalize() method
# returns a string where the first character is upper case, and the rest is lower case.
# syn:string.capitalize()
name = 'praveen'

print(name)
# praveen
print(name.capitalize())
# Praveen


# The casefold() method returns a string where all the characters are lower case.
#
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

print(name.casefold())
# praveen

location = 'CHENNAI'
print(location.casefold())
# chennai

