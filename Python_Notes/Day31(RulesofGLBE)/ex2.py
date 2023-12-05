# GLobal rule

a1 = 10
def fun1():

    def fun2():

        print('global variable:',a1)  # print function we are using in local scope in that, global variable present here
    fun2()
fun1()
