
x1 = [1,2,3,-4,-7,-10,4,2,6,-7,7,8,-3,-6,-5]
# print the zero's  instead of negetive numbers

# for i in range(len(x1)):
#     if x1[i]<0:
#         x1[i]=0
#         print(x1)


x2 = [1,2,3,4,5,9,8,7,6,4,3,2,1,2,3,4,6,8,9,7,4,3,2,5]
dict1 = {}

for i in x2:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1

print(dict1)
# {1: 2, 2: 4, 3: 4, 4: 4, 5: 2, 9: 2, 8: 2, 7: 2, 6: 2}

