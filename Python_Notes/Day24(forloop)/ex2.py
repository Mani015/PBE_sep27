# How  to stored into a new list (even & odd number)
even = []
odd = []
print('before even list:',even)
print('before odd list:',odd)
for i in range(1,11):
    if i%2==0:
        even.append(i)
        # print('loop excutes:',even)
    else:
        odd.append(i)

print('After even list:',even)
print('After odd list:',odd)

# before even list: []
# before odd list: []
# After even list: [2, 4, 6, 8, 10]
# After odd list: [1, 3, 5, 7, 9]
