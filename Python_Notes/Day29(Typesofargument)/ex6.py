
# ARBITRARY KEYWORD ARGUMENTS IN PYTHON
# For arbitrary positional argument, a double asterisk (**) is placed before a parameter
# in a function which can hold keyword variable-length arguments.


def New_dict(**velu):

    print(velu)
# New_dict(a=1,b=2,c=3,d=4,e=5)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


def New_dict1(**velu):
    for i in velu.items():
        print(i)

New_dict1(a='mango',b='banana',c='orange',d='graphes')

# ('a', 'mango')
# ('b', 'banana')
# ('c', 'orange')
# ('d', 'graphes')

