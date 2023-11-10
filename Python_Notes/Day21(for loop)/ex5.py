
# Find out the number is prime number or not


num = int(input('Enter a number:'))

var = 0
# print('before :',var)
for i in range(1,num+1):
    if num % i == 0:
        var = var + 1
# print('After',var)

if var == 2:
    print(num,' is prime number')
else:
    print(num ,' not a prime number')