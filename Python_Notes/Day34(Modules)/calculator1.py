
# from calculator import Addition,Subraction

from calculator import *

num1 = int(input('Enter 1st number:'))
num2 = int(input('Enter 2nd number: '))

Value = int(input('Enter 1 is addition; enter 2 is subtraction:'
                  ',enter 3 is multiplication:, enter 4 is division:'))


if Value==1:
    print(Addition(num1,num2))

elif Value==2:
    print(Subraction(num1,num2))

elif Value==3:
    print(Multiplication(num1,num2))
elif Value == 4:
    print(Division(num1,num2))

else:
    print('User enter invalid input')



