num = int(input('Enter a number:'))

def Main():
    if num % 2 == 0:
        def Fun1():
            print('even number')
    else:
        def Fun1():
            print('odd number')
    return Fun1()
Main()
# Enter a number:12
# even number
