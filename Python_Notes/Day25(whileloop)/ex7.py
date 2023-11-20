
# Find the sum of reverse numbers
num = int(input('Enter into a number:'))
sum = 0
while num != 0:
    digit = num%10
    print(digit,end='')
    sum = sum + digit
    num = num//10

print()
print('sum of numbers:',sum)
# Enter into a number:2443546
# 6453442
# sum of numbers: 28
