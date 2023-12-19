

# How to call method:
# sy: objectname.methodname()


class Person:
    def Method1(self):
        print('I am a Instance method')
        return 'Self is a current object'

# with out object creation
v1 = Person
# v1.Method1()
# TypeError: Method1() missing 1 required positional argument: 'self'


# with object creation

# v2 = Person()
# v2.Method1()


# ob1 = Person()
# Person.Method1(ob1)

print(Person().Method1())


