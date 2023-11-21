
for i in range(1,11):
    if i == 7:
        continue
    print(i**2)


x1 = [1,2,3,-4,-7,-10,4,2,6,-7,7,8,-3,-6,-5]
print()
x2 =[]

for i in x1:
    if i < 0:
        continue
    x2.append(i)
print(x2)