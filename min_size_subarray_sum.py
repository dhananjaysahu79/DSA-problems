# smallest subarray with sum greater thamn k (GfG).

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
# of which the sum is greater than or equal to target. If there is no such subarray,
# return 0 instead.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# A naive solution would be be checking each and every possible subarray. O(n^2)

# An efficient way is the two pointer approach. O(n)

arr = list(map(int,input().split()))
k = int(input())
a = s = 0
mn = 99999
for b in range(len(arr)):
    s += arr[b]
    if s >= k:
        while s - arr[a] >= k:
            s -= arr[a]
            a+=1
        mn = min(mn, b-a+1)
if mn == 99999: mn = 0
print(mn)
