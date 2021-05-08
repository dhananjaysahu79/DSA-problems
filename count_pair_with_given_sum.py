# Given an array of N integers, and an integer s,
# find the number of pairs of elements in the array whose sum is equal to s.
# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation:
# arr[0] + arr[1] = 1 + 5 = 6
# and arr[1] + arr[3] = 5 + 1 = 6.

# O(n) solution

arr = list(map(int,input().split()))
s = int(input())
dic = {}
ans = 0
for i in arr:
    if i in dic: dic[i] += 1
    else: dic[i] = 1
for i in arr:
    temp = s - i
    if temp in dic:
        if temp == i:
            ans += dic[temp] - 1
        else: ans += dic[temp]
print(ans // 2)