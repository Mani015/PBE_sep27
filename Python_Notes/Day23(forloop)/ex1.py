

l1 = [1,2,12.0,3.50,True,'hello','python',2+5j]
num = 0
Float  = 0
Bool = 0
Str = 0
Complex = 0

for i in l1:
    if type(i) == int:
        num+=1
    elif type(i) == float:
        Float+=1
    elif type(i) == bool:
        Bool+=1

    elif type(i) == str:
        Str+=1
    elif type(i) == complex:
        Complex+=1
    else:
        print("No Undefiend values")

print('Total number of int:',num)
print('Total number of float:',Float)
print('Total number of Bool:',Bool)
print('Total number of Strings:',Str)
print('Total number of complex:',Complex)

# Total number of int: 2
# Total number of float: 2
# Total number of Bool: 1
# Total number of Strings: 2
# Total number of complex: 1