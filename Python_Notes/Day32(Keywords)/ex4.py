# How to get local variable to the outside of the function without using global keyword
def fun1():
    l1 = 10
    l2 = 20
    l3 = 30
    l4 = 40
    v1 = locals()
    return v1

x1 = fun1()
print(x1)
# {'l1': 10, 'l2': 20, 'l3': 30, 'l4': 40}

for i in x1.values():
    if i > 20:
        print(i)

# 10
# 20
# 30
# 40

