

# a1 = 10  # global
# def f1():
#     a1 = 20 # enclosing
#     def f2():
#          # local scope
#         print('GV:',a1)
#         print(a1)
#     f2()
# f1()



# How to get value with the same name in global and local



# g1 = 'gangadharam'
# print('global variable:',g1)
# def fun1():
#     g1 = 'velu'
#     print('global variable:',g1)
# fun1()
# print('global variable:',g1)
# global variable: gangadharam
# global variable: velu
# global variable: gangadharam



# TO get global value inside of the function by using globals()
g1 = 'gangadharam'
print('global variable:',g1)
def fun1():
    g1 = 'velu'  # local variable
    print('local variable:',g1)
    print('global variable:', globals()['g1'])

fun1()
print('global variable:',g1)

# global variable: gangadharam
# local variable: velu
# global variable: gangadharam
# global variable: gangadharam

