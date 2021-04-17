# Maximum sum ascending subsequence
# example : 2 202 2 3 200 4 5
# output : 205
# we need to find out the subsequence which should be in ascending order with maximum sum
# Python 3 solution

arr = list(map(int,input().split()))
mx = 0; s = arr[0]
for i in range(1,len(arr)):
    if arr[i] > arr[i-1]: s += arr[i]
    else: s = arr[i]
    if s > mx: mx = s
print(mx)