# Using multipledispatch module to overcome methodoverloading
# Go to terminal
# pip install module name
# pip install multipledispatch
from multipledispatch import dispatch
class Compact:
    @dispatch(int,int)
    def Method1(self,a,b):
        return a + b

    @dispatch(int, int,int)
    def Method1(self,a,b,c):
        return a + b +c
    @dispatch(int,int,int,int)
    def Method1(self,a,b,c,d):
        return a + b + c +d


ob1 = Compact()
print(ob1.Method1(1,2))
print(ob1.Method1(11,22,33))