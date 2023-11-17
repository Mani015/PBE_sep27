# How to remove duplicate values in list
l1 = [1,2,3,4,2,1,3,4,5,6,7,6,5,3,25,7,9,0]
# print(l1)

s1 = set(l1)
l2 = list(s1)
# print(l2)
# [0, 1, 2, 3, 4, 5, 6, 7, 9, 25]


m1 = [1,2,3,4,2,1,3,4,5,6,7,6,5,3,25,7,9,0]
m2 = []
print('Before list:',m2)
for i in m1:
    if i not in m2:
        m2.append(i)
print('After list:',m2)
# Before list: []
# After list: [1, 2, 3, 4, 5, 6, 7, 25, 9, 0]
