
# Map With filter


x = sum(map(lambda var : var **2,filter(lambda num : num%2==0,range(1,21))))
# 1540
# print(x)

print((lambda var : 'even number' if var%2==0 else 'odd number')(x))
# even number

print(tuple(filter(lambda num :  num%2==0 ,[x])))



