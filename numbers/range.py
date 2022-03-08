"""
Play with range function in python
"""

# Play 1
def play1():
    # take a number and print next 20 consecutive numbers
    # Example: input=10, print: 10, 11, 12, 13.....30
    n=int(input("Enter your number:"))
    for i in range(n, n+20+1):
        print(i)

# Play 2
def play2():
    # Iterate a loop for the list items count times
    ll = [12, "345", "abc", "56", 45]
    n = len(ll)
    print(f"In list there is {n} items")
    for i in range(1, n+1):
        print(f"Iteratation-{i}")

if __name__ == '__main__':
    """ main function to execute test case """
    command=input("Enter your Play as play1, play2, play3 etc:")
    if command=="play1":
        play1()
    elif command=="play2":
        play2()
