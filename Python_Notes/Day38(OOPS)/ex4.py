# How to update Attribute value

class Student(object):
    name = 'Arjun'
    age = 20
    marks = 100
    location = 'chennai'

# sy: classname.attributename = new value

print('before name : ',Student.name)
# before name :  Arjun

Student.name = 'Velu'
print('After name : ',Student.name)
# After name :  Velu

# How to delete Attribute, by using del keyword
print()
print(Student.age)

# sy: del classname.attributename

del Student.age
print(Student.age)
# AttributeError: type object 'Student' has no attribute 'age'
