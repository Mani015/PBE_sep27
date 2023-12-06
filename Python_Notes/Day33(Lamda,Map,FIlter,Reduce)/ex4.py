
# The filter() Function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.
#
# As the name suggests, filter() forms a new list that contains only elements
# that satisfy a certain condition, i.e. the function we passed returns True.

# syn: filter(function_name,iterable)

n1 = {1,2,3,-2,6,-7,-1,4,5,7,6,-7,-10}

def Postive_numbers(char):
    if char > 0:
        return True

number = filter(Postive_numbers,n1)
# print(list(number))



def Ends_with_name(boo):
    if boo.endswith('ing'):
        return True


names = tuple(filter(Ends_with_name,['Moring','walking','entertainment','chill','happy','advance']))
print(names)
# ('Moring', 'walking')



