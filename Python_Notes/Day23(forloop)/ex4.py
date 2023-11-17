
# Find out the vowels in the given string

quoatation = input('Enter a string:')

count = 0

for i in quoatation:
    if i in 'AEIOUaeiou':
        count+=1

print('Total vowels in a given string:',count)
# Enter a string:i am good In mathematics
# Total vowels in a given string: 9
