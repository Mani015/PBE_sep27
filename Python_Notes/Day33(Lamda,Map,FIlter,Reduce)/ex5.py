

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

# print(list(filter_object))
# ['Apple', 'Apricot']


# Filter with lambda

# syntax:  filter(function_name,iterable)
# example: filter(lambda var : var[0],furit)

print(list(filter(lambda var :  var[0]=='A' ,fruit)))

# ['Apple', 'Apricot']


