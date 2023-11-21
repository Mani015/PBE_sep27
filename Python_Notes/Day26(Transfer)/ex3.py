
attempt = 0

while attempt < 4:
    password = int(input('Enter your password:'))
    if password == 1234:
        print('Screen is open')
        break
    else:
        print('you have enterd wrong password! please try again')
        attempt+=1

else:
    print('Your limits is completed')