
# Built-in scope:

g1 = 10  # Global Scope
print('G V:',g1)
def Fun1():
    non = 20 # Enclosing/Non-local scope
    print('E V:',non)
    def Fun2():
        l1 = 30  # Local scope
        print('L V:',l1)
        var = [g1,non,l1]
        print('sum of:',sum(var))
    Fun2()
Fun1()
# G V: 10
# E V: 20
# L V: 30
# sum of: 60


# min()
# max()
# len()
# sum()
# all()
# print()
