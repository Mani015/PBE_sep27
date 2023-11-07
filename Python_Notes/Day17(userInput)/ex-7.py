# Find out the Percentage of Student:

# 1st we have take 6 user inputs


sub1 = eval(input('Enter sub1 marks:'))
sub2 = eval(input('Enter sub2 marks:'))
sub3 = eval(input('Enter sub3 marks:'))
sub4 = eval(input('Enter sub4 marks:'))
sub5 = eval(input('Enter sub5 marks:'))
sub6 = eval(input('Enter sub6 marks:'))
# Adding the Total subject marks:

Sum = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print('Student total marks:',Sum)

# percentage :
# formula:  (sum of marks/ Total marks) * 100

percentage = (Sum/600) * 100
print('Student percentage:',percentage)

# Enter sub1 marks:99
# Enter sub2 marks:89
# Enter sub3 marks:85
# Enter sub4 marks:100
# Enter sub5 marks:96
# Enter sub6 marks:95
# Student total marks: 564
# Student percentage: 94.0







