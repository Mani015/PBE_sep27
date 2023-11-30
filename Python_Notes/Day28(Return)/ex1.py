# Function inside value , you have to get outside of the function using return keyword

def Add_numbers(a,b,c):
    result = a + b + c
    return result


var = Add_numbers(6,7,10)
print(var)
for i in range(1,11):
    print(f'{var} x {i} = {var * i}')

