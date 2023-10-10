
# The count() method returns the number of times a specified value appears in the string.

s1 = "Nothing is more expansive then a missed oppurtunity"

# syn: string.count(value)

print(s1.count('is'))
# 2
print(s1.count('i'))
# 5
# syn: string.count(value,start,end)
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string

print(s1.count('i',6))
# 4

print(s1.count('i',1,5))
# 1

print(s1.count('t'))
# 4
print(s1.count('t',10))
# 3

print(s1.count('N'))
# 1
