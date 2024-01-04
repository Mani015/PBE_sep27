
class Employee:   # Parent class
    def __init__(self,Ename,Eage,Esalary,Elocation,Edomain):
        self.name = Ename
        self.age = Eage
        self.Salary = Esalary
        self.location = Elocation
        self.domain = Edomain

class Fresher(Employee):
    def __init__(self, Ename, Eage, Esalary, Elocation, Edomain, Efresher):
        Employee.__init__(self,Ename,Eage,Esalary,Elocation,Edomain)
        self.fresher = Efresher

    def Dispaly(self):
        print(
            self.name, self.age,
            self.Salary, self.location, self.domain, self.fresher
        )

class Ex_Employee(Employee):
    def __init__(self, Ename, Eage, Esalary, Elocation, Edomain, Eexperience, Estatus):
        super().__init__(Ename,Eage,Esalary,Elocation,Edomain)
        self.exp = Eexperience
        self.status = Estatus

    def Dispaly(self):
        print(
            self.name, self.age,
            self.Salary, self.location, self.domain,
            self.exp, self.status
        )

ob2 = Ex_Employee('Velu',23,50000,'chennai','PFD','2+years','Married')
ob2.Dispaly()






















ob1 = Fresher('Velu',23,50000,'chennai','PFD','yes')
ob1.Dispaly()



