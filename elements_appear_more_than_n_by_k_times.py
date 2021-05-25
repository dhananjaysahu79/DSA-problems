# Print all the elements whose count is greater than n/k.
# Input: 3 2 3 2 4 2 3 4
#        4
# Output: 3 2
# O(n) solution

arr = list(map(int,input().split()))
k = int(input())
dic = {}
for i in arr:
    if i in dic: dic[i] += 1
    else: dic[i] = 1
print(*[i for i,j in dic.items() if j > len(arr) // k])