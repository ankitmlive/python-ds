"""
Python programme for linear search
The time complexity of the above algorithm is O(n), because it checks each element in list
"""

def linear_search(arr, num):
    n=len(arr)
    for i in range(n):
        if arr[i]==num:
            return i
    return -1

if __name__=="__main__":
    arr=[29, 56, 78, 64, 23, 87, 69, 40]
    num=23
    position=linear_search(arr, num)
    print(f"Position of {num} in given array is {position}")
