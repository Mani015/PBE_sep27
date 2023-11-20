
# Print 1st 20 numbers, which are divisible by 4 and 9

num = 1
i = 0

while i <= 20:
    if num%4==0 and num%9==0:
        print(num)
        i+=1
    num  = num + 1

print('loop complete')