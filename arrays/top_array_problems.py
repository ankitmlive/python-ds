# Best time to buy and sell stock

prices = [7, 1, 5, 3, 6, 4]

def Max(arr):
    l, r = 0, 1
    maxp = 0

    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            maxp = max(maxp, profit)
        else:
            l = r
        r += 1
    return maxp

p = Max(prices)
print(p)
