
# @staticmethod
# Transform a method into a static method.
#
# A static method does not receive an implicit first argument. To declare a static method, use this idiom:
#
# class C:
#     @staticmethod
#     def f(arg1, arg2, argN): ...
# The @staticmethod form is a function decorator – see Function definitions for details.

class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))

# We generally use static methods to create utility functions.
