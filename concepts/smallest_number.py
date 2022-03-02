def FindSmallest(arr):
    min1 = arr[0]
    for i in range(len(arr)):
        if arr[i] < min1:
            min1 = arr[i]
    return min1

n = int(input())
arr = list(map(int, input().split()))
 
out_ = FindSmallest(arr)
print (out_)