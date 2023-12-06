
# Convert the iterable values from lower case to upper case

def Ultra(names):
    return names.upper()

name = map(Ultra,{'gangadharam','velu','karthik','penchalya','ramu','prasad'})
# print(list(name))
# ['VELU', 'RAMU', 'KARTHIK', 'PENCHALYA', 'GANGADHARAM', 'PRASAD']


# map with lambda


# print(map(lambda name : name.lower(),['ONE','TWO','THREE','FOUR']))
# <map object at 0x0000013D3AE41AF0>


print(list(map(lambda name : name.lower(),['ONE','TWO','THREE','FOUR'])))

# ['one', 'two', 'three', 'four']
