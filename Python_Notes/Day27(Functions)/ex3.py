# Passing Parameters when defining a function

# sy:
# def functionname(par1,par2,.......parN):
    # body of function

# functionname(arg1,agr2,arg.........N)


def Techno(a,b):
    print('a values is:',a)
    print('b value is:',b)
# Techno()
# TypeError: Techno() missing 2 required positional arguments: 'a' and 'b'

# Techno(10)
#TypeError: Techno() missing 1 required positional argument: 'b'

Techno(12,14)
# a values is: 12
# b value is: 14
print()
Techno('velu','gangadharam','raju')
# TypeError: Techno() takes 2 positional arguments but 3 were given
