

def Student(name,age,location):
    print('student name:',name)
    print('student age:',age)
    print('student location:',location)


# Student(21,location='tiruapthi',name='velu')
# TypeError: Student() got multiple values for argument 'name'
# Student(21,location='madurai',age='velu')
# student name: 21
# student age: velu
# student location: madurai


age = 'Ramu'
location = 23
name = 'india'

Student(name=age,location=name,age=location)
# student name: Ramu
# student age: 23
# student location: india
