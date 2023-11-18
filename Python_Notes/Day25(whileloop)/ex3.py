num=0
i=0
sum=0
while i<10:
    if num%7==0:
        print(num)
        sum+=num
        i+=1
    num+=1
print("sum value",sum)
print("Avarage",sum/i)

# 0
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# sum value 315
# Avarage 31.5
