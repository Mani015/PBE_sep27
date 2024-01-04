# ename,eage,esalary,elocation,edomain,eexperience,maritial status,



class Employee:
    def __init__(self,Ename,Eage,Esalary,Elocation,Edomain,Eexperience,Estatus):
        self.name = Ename
        self.age = Eage
        self.Salary = Esalary
        self.location = Elocation
        self.domain = Edomain
        self.exp = Eexperience
        self.status = Estatus
    def Dispaly(self):
        print(
            self.name,self.age,
            self.Salary,self.location,self.domain,
            self.exp,self.status
        )


ob1 = Employee('Velu',23,50000,'chennai','PFD','2+years','Married')
ob1.Dispaly()
# Velu 23 50000 chennai PFD yes
