# buy and sell stocks at most twice such that profit can be maximized
# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75
# Buy at 10, sell at 22,
# Buy at 5 and sell at 80


# Naive solution O(n^2) time complexity

# Approach : we would be splitting the array in two in a certain ratio
# and we will check maximum profit out of those splitted arrays.
# and then we will find the maximum of those sums.
# the function maxProfit is calculating the maxProfit in each splitted array same
# as `best time to sell a stock` problem.


def maxProfit(arr):
    if len(arr) < 2: return 0
    maxi = 0; curr_stock = arr[0]
    for i in arr[1:]:
        maxi = max(maxi, i - curr_stock)
        if i < curr_stock: curr_stock = i
    return maxi

arr = list(map(int,input().split()))
mx = 0
for i in range(len(arr)-1):
    mx = max(maxProfit(arr[:i]) + maxProfit(arr[i:]), mx)
print(mx)

# O(n) Approach
# So in the first iteration we will move backward and find the maximum profit
# at the particular index.
# Then we will iterate from forward to find the maximum at particular index + we will add
# maximum profit generated after that index.(simply breaking the array in two subsequence of differrent sizes)

arr = list(map(int,input().split()))
n = len(arr)
maxi = [0] * n
mx = arr[n-1]
for i in range(n-2, 0, -1):
    mx = max(mx, arr[i])
    maxi[i] = max(maxi[i+1], mx - arr[i])
mn = arr[0]
for i in range(1,n):
    mn = min(arr[i], mn)
    maxi[i] = max(maxi[i-1], arr[i] - mn + maxi[i])
print(maxi[-1])
