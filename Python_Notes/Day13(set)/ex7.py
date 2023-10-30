# The remove() method removes the specified element from the set.
#  syntax:-
#  set.remove(item)
s1={'jonh','raju','divya','kartik','ramu','raj','velu','gangadhar'}
print(s1)
# {'divya', 'kartik', 'velu', 'gangadhar', 'jonh', 'raj', 'raju', 'ramu'}

s1.remove('jonh')
print(s1)
# {'kartik', 'ramu', 'divya', 'raj', 'gangadhar', 'velu', 'raju'}


# s1.remove('aryan')
# print(s1)
# KeyError: 'aryan'


s1.discard('aryan')
print(s1)
# {'raj', 'velu', 'divya', 'gangadhar', 'kartik', 'raju', 'ramu'}