
# extend:Add the elements of a list (or any iterable), to the end of the current list
list=[1,2,3,4,5,6]
list.extend([7,8,9])
print(list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert:Adds an element at the specified position

list.insert(3,8)
print(list)
# [1, 2, 3, 8, 4, 5, 6, 7, 8, 9]

# pop:Removes the element at the specified position
list.pop(3)
print(list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list.pop(12)
print(list)
# IndexError: pop index out of range