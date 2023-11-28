# A fucntion with in the another function
# def Fun1(a): # outer function
#     var1 = a
#     def Fun2(b,c): # Inner function
#         var2 = b + c
#         return var2
#     print(Fun2(12,13))
# Fun1(11)
# 25



# def Fun1(a): # outer function
#     var1 = a
#     def Fun2(b,c): # Inner function
#         var2 = b + c
#         return var2
#     return Fun2(12,13)
# print(Fun1(11))



def Fun1(a): # outer function
    var1 = a
    def Fun2(b,c): # Inner function
        new = b + c
        return new
    var2 = Fun2(12,13)
    var3 = var2 + var1
    return var3


num = Fun1(11)

if num%2==0:
    print(num,'even number')
else:
    print(num,'odd number')

