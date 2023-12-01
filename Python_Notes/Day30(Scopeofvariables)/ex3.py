# Enclosing variable:
# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.
# If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function.
# This scope contains the names that you define in the enclosing function.
# The names in the enclosing scope are visible from the code of the inner and enclosing functions.

g1 = 10 # global variable
print('global scope:',g1)
def fun1():
    e1 = 20  # enclosing variable
    print('enclosing scope:',e1)
    print('global scope:', g1)
    def fun2():
        l1 = 30  # local scope
        print('local scope:',l1)
        print('global scope:', g1)
        print('enclosing scope:', e1)
    fun2()
    print('global scope:', g1)
    print('enclosing scope:', e1)
fun1()


# global scope: 10
# enclosing scope: 20
# global scope: 10
# local scope: 30
# global scope: 10
# enclosing scope: 20
# global scope: 10
# enclosing scope: 20
