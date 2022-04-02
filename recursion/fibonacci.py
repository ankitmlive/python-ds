"""
A Fibonacci is a number series, in which next number will be the sum of previous two values. 
Example:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144..
Rule: The Rule is xn = xn-1 + xn-2
This is a Fibonacci programme using recursion
"""

def fibonacci(n):
    # base case
    if n <= 1:
        return n
    # calling the function recursively
    return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    n=int(input("Please enter a digit to calculate sum of fibonacci: "))
    ans = fibonacci(n)
    print(f"Fibonacci of {n} is {ans}")