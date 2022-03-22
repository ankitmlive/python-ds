"""
Python programme for binary search
Time complexity: Best: O(1), Average: O(log n), Worst: O(log n)
Space complexity: O(1)
Algorithm: It uses the divide and conquer approch,
    1: get first, last and mid of the array
    2: if mid==value, return the value otherwise compare the value it is either left side or right side
    3: This implementation is created using recursive approach for practice
"""

def binary_search_recursive(arr, first, last, num):
    """ Binary Search using Recursive approach """
    if first < last:

        # get the mid of the array
        mid = (first+last)//2

        # retunr the number if mid == num
        if num == arr[mid]:
            return mid
        
        if num < arr[mid]:
            return binary_search_recursive(arr, 0, mid-1, num)
        else:
            return binary_search_recursive(arr, mid+1, last, num)
    else:
        return None

if __name__=="__main__":
    input_num = int(input("Please Input number to be searched from the given list: "))
    arr=[23, 36, 48, 54, 63, 77, 89, 90]
    position=binary_search_recursive(arr, 0, len(arr)-1, input_num)
    print(f"Position of {input_num} in given array is {position}")