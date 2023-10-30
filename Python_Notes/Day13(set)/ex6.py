# The update() method updates the current set,
# by adding items from another set (or any other iterable)

# syntax:-
# set.update(set)
fruits={'apple','mango','grapes','orange','pineapple'}
print(fruits)
# {'orange', 'apple', 'mango', 'pineapple', 'grapes'}

fruits.update({'banana','kiwi','water melon','papaya'})
print(fruits)
# {'banana', 'papaya', 'apple', 'kiwi', 'pineapple', 'grapes', 'orange', 'water melon', 'mango'}


