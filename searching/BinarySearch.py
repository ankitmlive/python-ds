"""
Python programme for binary search
Time complexity: Best: O(1), Average: O(log n), Worst: O(log n)
Space complexity: O(1)
Algorithm: It uses the divide and conquer approch,
    1: get first, last and mid of the array
    2: if mid==value, return the value otherwise compare the value it is either left side or right side
    3: This implementation is created using iterative approach because recursion perfomrs very poor in Python
"""

def binary_search(arr, num):
    n=len(arr)
    first=0
    last=n-1
    while(first <= last):
        mid=(first+last)//2
        if num==arr[mid]:
            return mid
        if num < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return None

if __name__=="__main__":
    input_num = int(input("Please Input number to be searched from the given list: "))
    arr=[23, 36, 48, 54, 63, 77, 89, 90]
    position=binary_search(arr, input_num)
    print(f"Position of {input_num} in given array is {position}")