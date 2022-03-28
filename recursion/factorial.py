"""
A Factorial is a product off all number for a given number
Example: fact(5) = 5*4*3*2*1
This is a factorial programme using recursion
"""

def factorial(n):
    # base case
    if n == 1:
        return 1
    # calling the fucntion recursively
    return n * factorial(n-1)
    
if __name__ == "__main__":
    n=int(input("Please enter a digit to calculate factorial: "))
    ans = factorial(n)
    print(f"Factorial of {n} is {ans}")
