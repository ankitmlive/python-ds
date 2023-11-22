# by sorting
def minmix(arr):
  arr.sort()
  return arr[0], arr[len(arr)-1]


# by linear search
def minmax(arr):
    rmin, rmax = 0, 0
    if arr[0] > arr[1]:
        rmax = arr[0]
        rmin = arr[1]
    else:
        rmax = arr[1]
        rmin = arr[0]
    
    for i in range(2, len(arr)):
        if rmax < arr[i]:
            rmax = arr[i]
        if rmin > arr[i]:
            rmin = arr[i]

    return rmin, rmax
