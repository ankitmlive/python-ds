"""
A Simple programme to understand recursion.
A recursive function consist of a base case and call to himself logic
This programm will print "Hello", 10 times using recursion
"""

def printHello(n):
    # base case
    if n == 0:
        return
    print("Hello")
    # calling the fucntion again
    printHello(n-1)
    
if __name__ == "__main__":
    n=10
    print("It will print \"Hello\" for 10 Times")
    printHello(n)
