

class Student(object):
    Schoolname = 'New Horizon'  # class variable
    def __init__(self,sname,sage,smarks,slocation):
        self.name = sname
        self.age = sage
        self.marks = smarks
        self.location = slocation


ob1 = Student('Rajesh',20,83,'pune')
ob2 = Student('Vinod',23,95,'mumbai')
ob3 = Student('Ramu',24,96,'kerala')
ob4 = Student('Vidyasagar',23,78,'chennai')

for i in [ob1,ob2,ob3,ob4]:
    print('Sname : ',i.name)
    print('Sage:',i.age)
    print('Smarks : ',i.marks)
    print('Slocation : ',i.location)
    print('Schoolname : ',Student.Schoolname)
    print('----------><----------')

# Sname :  Rajesh
# Sage: 20
# Smarks :  83
# Slocation :  pune
# Schoolname :  New Horizon
# ----------><----------
# Sname :  Vinod
# Sage: 23
# Smarks :  95
# Slocation :  mumbai
# Schoolname :  New Horizon
# ----------><----------
# Sname :  Ramu
# Sage: 24
# Smarks :  96
# Slocation :  kerala
# Schoolname :  New Horizon
# ----------><----------
# Sname :  Vidyasagar
# Sage: 23
# Smarks :  78
# Slocation :  chennai
# Schoolname :  New Horizon
# ----------><----------


