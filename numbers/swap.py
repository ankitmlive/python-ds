def swap(a, b):
    """
    Simple swapping function
    Swap the element if fisrt element is greter than second one
    """
    if a > b:
        a, b = b, a
    return a, b
    

print("No Swapping performed", swap(3, 6))
print("Swaping Performed", swap(6, 4))
print("Swaping Performed", swap(27, 18))