
# The nonlocal keyword is used to work with variables inside nested functions,
# where the variable should not belong to the inner function.
# Use the keyword nonlocal to declare that the variable is not local.


# def fun1():
#     en = 10
#     print('EV:',en)
#     def fun2():
#         l1 = 20
#         print('LV:',l1)
#         print('EV:', en)
#     fun2()
#     print('EV:', en)
# fun1()

# EV: 10
# LV: 20
# EV: 10
# EV: 10



# With nonlocal statement


def fun1():
    en = 10
    print('EV:',en)
    def fun2():
        nonlocal en
        en = 20
        print('LV:',en)

    fun2()
    print('EV:', en)
fun1()

# EV: 10
# LV: 20
# EV: 20