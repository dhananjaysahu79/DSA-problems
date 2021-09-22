# Solution 1: O(n^2)

arr = list(map(int, input().split()))
dp = [0] * len(arr)
for i in range(len(arr)):
    sm = 0
    for j in range(i):
        if arr[i] > arr[j]: sm = max(sm, dp[j])
    dp[i] = sm + arr[i]
print(max(dp))