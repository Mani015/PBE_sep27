
# Find out sum of 1st 10 natural number


sum = 0
iterations = 0
for i in range(1,11):
    sum  = sum + i
    iterations = iterations + 1

print(sum)

print(iterations)
ave = sum//iterations
print(ave)