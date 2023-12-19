
# In Python, a constructor is a special type of method used to initialize the object of a Class.

class Employee(object):
    # A constructor is optional, and if we do not provide any constructor, then Python provides the default constructor.
    # Every class in Python has a constructor, but it's not required to define it.
    #
    #
    # def __init__(self):
    #     # body of the constructor
    def __init__(self,Ename,Eage,Esalary,Edomain,Elocation):
        #self.New_variable_name = parameter
        # object.NewVariable_name = Parameter
        self.name = Ename  # vikas
        self.age = Eage # 20
        self.salary = Esalary
        self.domain = Edomain
        self.location = Elocation
        print(self.name)
        print(self.age)
        print(self.domain)
        print(self.salary)
        print(self.location)
        print()

Employee('vikas',20,20000,'PFS','Kerala')  #The constructor will be executed automatically when the object is created

# vikas
# 20
# PFS
# 20000
# Kerala



# def: The keyword is used to define function.
# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
# self: The first argument self refers to the current object. It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.



# If we create three objects,
# the constructor is called three times and initialize each object.
print('object2:')
Employee('Karthik',21,30000,'JFS','Mumbai')
print('object3:')
Employee('Ramu',22,40000,'Database','Chennai')
