l4=['hema','john',3,6,77,8.5,67,]
print(l4[1:5])
print(l4[0::])
print(l4[::-1])
# ['john', 3, 6, 77]
# ['hema', 'john', 3, 6, 77, 8.5, 67]
# [67, 8.5, 77, 6, 3, 'john', 'hema']

# methods in list
# Append:Adds an element at the end of the list
l5=[1,2,3,4,5]
l5.append(6)
print(l5)
# count:Returns the number of elements with the specified value
l6=[12,43,56,77,43,56,12,12]
print(l6.count(12))

# clear:Removes all the elements from the list
l6.clear()
print(l6)
# []

# copy:Returns a copy of the list
list=[3,55,76,89,45,33]
new_list=list.copy()
print(new_list)
# [3, 55, 76, 89, 45, 33]


