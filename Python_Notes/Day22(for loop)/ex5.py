# Find out the how many odd & even numbers between 1, and 21

even_num = 0
odd_num = 0
for i in range(1,21):
    if i%2==0:
        even_num = even_num + 1

    else:
        odd_num = odd_num + 1

print('Total evenumber :',even_num)
print()
print('Total number of odd numbers:',odd_num)
# Total evenumber : 10
#
# Total number of odd numbers: 10
