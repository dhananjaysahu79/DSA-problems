# Given an array arr of size n and an integer k. Find if there's a triplet in the array
# which sums up to the given integer k.
# Input:
# n = 6, k = 13
# arr[] = [1 4 45 6 10 8]
# Output:
# True
# Explanation:
# The triplet {1, 4, 8} in
# the array sums up to 13.

# A naive approach would be O(n^3) time complexity.
# An optimised approach is to take a set and taking one element
# as constant for each value of i.

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
ans = False
for i in range(n-2):
    s = set()
    for j in arr[i+1:]:
        if j in s:
            ans = True
            break
        s.add(k-arr[i]-j)
    if ans: break
print(ans)