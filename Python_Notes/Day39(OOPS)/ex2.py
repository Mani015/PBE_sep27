
# To call attributes using object


class Employee:
    def __init__(self, Ename, Eage, Edomain, Elocation, Eemail, Esalary):
        self.name = Ename   #ob1.name
        self.age = Eage
        self.domain = Edomain
        self.location = Elocation
        self.email = Eemail
        self.salary = Esalary

ob1 = Employee('Prasanth',25,'DjangoDeveloper','chennai','prasanth@gmail.com',30000)
# syn: object_name.Attribute_name

print(ob1.name)
print(ob1.age)

# Prasanth
# 25


print(Employee('Prasanth',25,'DjangoDeveloper','chennai','prasanth@gmail.com',30000).name)
#