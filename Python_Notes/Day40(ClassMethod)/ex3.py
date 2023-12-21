
# How to call class varible by using instance method


class Student(object):
    Schoolname = 'New Horizon'  # class variable
    def __init__(self,sname,sage,smarks,slocation):
        self.name = sname
        self.age = sage
        self.marks = smarks
        self.location = slocation
    def Call_class_Variable(self):
        print(
            self.name, self.age, self.marks, self.location,self.Schoolname
        )


ob2 = Student('Vinod',23,95,'mumbai')
ob2.Call_class_Variable()
# Vinod 23 95 mumbai New Horizon
