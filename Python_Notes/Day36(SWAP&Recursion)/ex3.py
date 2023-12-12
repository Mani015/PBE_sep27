
def fun():
    print('Hello function')
    fun()   # function calling it self
# fun()
# RecursionError: maximum recursion depth exceeded while calling a Python object



def f1():
    print('hello ramu ji')
# print(type(f1))
# <class 'function'>
f1()

# What is the Recursion limit: getrecursionlimit()
import sys
print('Maximcum interpreter capacity:',sys.getrecursionlimit())
# Maximcum interpreter capacity: 1000

