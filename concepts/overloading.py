# ------> Method Overloading <----------#

""" Python Does not support method overloading, But there are different ways to achieve method overloading in Python.
The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.
"""

# A function
def add(a, b):
    var = a+b
    print(a+b)

# function overloading
def add(a, b, c):
    var = a+b+c
    print(var)

# Printing
# calling this function will give error, because the second mmethod will be called with 2 params only
# add(2,3) 

def add(a, b, *args):
    pass