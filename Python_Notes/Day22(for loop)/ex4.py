
t1 = (11,22,33,44,55)
print('before tuple:',t1)
print()
# t2 = reversed
# print(type(t2))

t2 = reversed(t1)

print('After tuple:',tuple(t2))
# After tuple: <reversed object at 0x000001D845570BB0>

# After tuple: (55, 44, 33, 22, 11)



for i in reversed(range(1,11)):
    print(i)

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
