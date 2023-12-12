
# 😀 😀 😀 😀 😀 😀 😀 😀 😀 😀
# 10  9  8  7  6   5  4   3  2   1



def Recursion(num):
    if num == 0:
        return 0
    else:
        return num + Recursion(num - 1)

print(Recursion(5))

