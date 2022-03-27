"""
A Simple programme to understand recursion.
A recursive function consist of a base case and call to himself logic
This programm will calculate the sum of n natural numbers.
"""

def CalculateSum(n):
    # base case
    if n == 1:
        return 1
    
    # calling the function again
    return n + CalculateSum(n-1)
    
if __name__ == "__main__":
    n = int(input("Please input a number to find sum of numbers: "))
    print("Answer is:", CalculateSum(n))
