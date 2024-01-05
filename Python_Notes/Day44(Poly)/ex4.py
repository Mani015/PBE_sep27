
# 1 class
# Multiple methods , but different parametes


class Compact:
    def Method1(self,a,b):
        return a + b
    def Method1(self,a,b,c):
        return a + b +c
    def Method1(self,a,b,c,d):
        return a + b + c +d


ob1 = Compact()
ob1.Method1(1,2)
# TypeError: Method1() missing 2 required positional arguments: 'c' and 'd'
