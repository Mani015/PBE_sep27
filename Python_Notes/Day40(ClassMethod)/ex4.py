
# How to update class variable using instance method



class Student(object):
    Schoolname = 'New Horizon'  # class variable
    def __init__(self,sname,sage,smarks,slocation):
        self.name = sname
        self.age = sage
        self.marks = smarks
        self.location = slocation

    def Update_Class_variable(self,NewName):
        self.Schoolname = NewName
        print(self.Schoolname)

    def Call_class_Variable(self):

        print(
            self.name, self.age, self.marks, self.location,self.Schoolname
        )

ob1 = Student('Vishal',22,100,'pune')
ob1.Call_class_Variable()
# Vishal 22 100 pune New Horizon

ob1.Update_Class_variable('Narayan School')

ob1.Call_class_Variable()
# Vishal 22 100 pune Narayan School
