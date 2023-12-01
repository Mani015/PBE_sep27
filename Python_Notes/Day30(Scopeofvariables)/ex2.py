
# Local variable: local variable is variable ,
# which is declared inside of the function is known as local variable.


# def fun():
#     name = 'velu'  # Local variable
#     print('Local var:',name)
# fun()
# Local var: velu


# We are trying to get the local variable outside of the function

def fun():
    name = 'velu'  # Local variable
    print('Local var:',name)
fun()
print('Local var:',name)
# NameError: name 'name' is not defined
# Local var: velu



# Local scope: The names that you define in this scope are only available or visible to the code within the scope.