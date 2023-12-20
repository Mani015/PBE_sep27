
# Instance variables: If the value of a variable varies from object to object, then such variables are called instance variables.
#
# Create Instance Variables
# Instance variables are declared inside a method using the self keyword.
class Employee:
    def __init__(self, Ename, Eage, Edomain, Elocation, Eemail, Esalary):
        self.name = Ename   # Instance variable 1
        self.age = Eage     # Instance variable 2
        self.domain = Edomain # Instance variable 3
        self.location = Elocation  ## Instance variable 4
        self.email = Eemail  # Instance variable 5
        self.salary = Esalary  # Instance variable 6
# We use a constructor to define and initialize the instance variables. Let’s see the example to declare an instance variable in Python.
#
# The self refers to the current object

 # We can access the instance variable using the object and dot (.) operator.
#
# When we create classes in Python, instance methods are used regularly.
# we need to create an object to execute the block of code or action defined in the instance method.
#
# Instance variables are used within the instance method. We use the instance method to perform a set of actions on the data/value provided by the instance variable.
#

#
# In Python, to work with an instance variable and method, we use the self keyword.
# We use the self keyword as the first parameter to a method. The self refers to the current object.