# The intersection() method returns a set that contains the similarity between two or more sets

# syntax:-set.intersection(set1, set2 ... etc)

name={'pawan','aakash','prakash','abhi'}
print(name)
# {'abhi', 'pawan', 'aakash', 'prakash'}
name1={'abhi','pawan','raju','shekhar'}
print(name1)
# {'abhi', 'pawan', 'shekhar', 'raju'}

name3=name.intersection(name1)
print(name3)
# {'pawan', 'abhi'}