

def Vowels(num):
    if num in 'aeiou':
        return num

# num = input('Enter a quotation:')
#
# v1 = set(filter(Vowels,num))
# print(v1)
# Enter a quotation:don't think negitivity
# {'e', 'i', 'o'}


# using lambda

print(list(filter(lambda char : char in 'aeiou',"don't think negitivity")))
# ['o', 'i', 'e', 'i', 'i', 'i']

