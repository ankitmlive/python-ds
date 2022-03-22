"""
Bubble Sort in Python
Used to sort an array, It itearte every element for input number
Time complexicity: O(n), O(n^2), O(n^2), Space Complexicity: O(1) 
"""

def BubbleSort(arr):
    """ Bubble Sort in Python """
    swapped = False
    n=len(arr)
    for i in range(n):
        # compare 1st and 2nd then all consecutive elements
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True

        if not swapped:
            print("Array is already sorted")
            break

if __name__ == "__main__":
    input_arr = [12,23,34,45,56,67,78,89,3,8,11,32,28]
    BubbleSort(input_arr)
    print("Sorted Elements:", input_arr)
