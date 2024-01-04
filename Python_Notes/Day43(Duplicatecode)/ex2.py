# ename,eage,esalary,elocation,edomain,efresher


class Employee:
    def __init__(self,Ename,Eage,Esalary,Elocation,Edomain,Efresher):
        self.name = Ename
        self.age = Eage
        self.Salary = Esalary
        self.location = Elocation
        self.domain = Edomain
        self.fresher = Efresher
    def Dispaly(self):
        print(
            self.name,self.age,
            self.Salary,self.location,self.domain,self.fresher
        )


ob1 = Employee('Velu',23,50000,'chennai','PFD','yes')
ob1.Dispaly()
# Velu 23 50000 chennai PFD yes
