
# Locals method

# Return a dictionary containing the current scope's local variables.


g1 = 10
print('Gv:',g1)
def fun1():
    l1 = 20
    print('LV:',l1)
    print('using locals method:',locals())
fun1()
# Return a dictionary containing the current scope's local variables.
