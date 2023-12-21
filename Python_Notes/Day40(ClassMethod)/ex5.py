

# Class variable deleted using istance method

class Student(object):
    Schoolname = 'New Horizon'  # class variable
    def __init__(self,sname,sage,smarks,slocation):
        self.name = sname
        self.age = sage
        self.marks = smarks
        self.location = slocation


    def Delete_class_variable(self):

        del Student.Schoolname


    def Call_Classvariable(self):
        print(self.name)
        print(self.age)
        print(self.location)
        print(Student.Schoolname)
        print()




ob1 = Student('Vishal',22,100,'pune')
ob1.Call_Classvariable()

#Vishal
# 22
# pune
# New Horizon

ob1.Delete_class_variable()

ob1.Call_Classvariable()
# AttributeError: type object 'Student' has no attribute 'Schoolname'


