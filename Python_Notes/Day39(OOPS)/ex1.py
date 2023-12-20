
# Ename,Eage,Edomain,Elocation,Eemail,Esalary

class Employee:
    def __init__(ramu, Ename, Eage, Edomain, Elocation, Eemail, Esalary):
        ramu.name = Ename
        ramu.age = Eage
        ramu.domain = Edomain
        ramu.location = Elocation
        ramu.email = Eemail
        ramu.salary = Esalary

    def Show(self):
        print(
            self.name,
            self.age,self.domain,
            self.salary,self.email,self.location
        )


ob1 = Employee('Prasanth',25,'DjangoDeveloper','chennai','prasanth@gmail.com',30000)
ob1.Show()
# Prasanth 25 DjangoDeveloper 30000 prasanth@gmail.com chennai


# TypeError: Employee() takes no arguments