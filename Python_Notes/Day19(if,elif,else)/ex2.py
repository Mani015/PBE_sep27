
# Chain multiple if statement in Python
# In Python, the if-elif-else condition statement has an elif blocks
# to chain multiple conditions one after another.
# This is useful when you need to check multiple conditions.
#
# With the help of if-elif-else we can make a tricky decision.
# The elif statement checks multiple conditions one by one and if the condition fulfills, then executes that code.
#
# Syntax of the if-elif-else statement:
#
# if condition-1:
#      statement 1
# elif condition-2:
#      stetement 2
# elif condition-3:
#      stetement 3
#      ...
# else:
#      statement


user = int(input('Enter a number'))

if user==1:
    print('If is True')
elif user==2:
    print('condition 2 is Correct ')
elif user == 3:
    print('Condition 3 is correct')
elif user == 4:
    print('Condition 4 is correct')
else:
    print('when the Above  conditions are false,else will excuted ')

# Enter a number5
# when the Above  conditions are false,else will excuted
