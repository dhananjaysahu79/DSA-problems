# Maximum sum ascending subsequence
# example : 2 202 2 3 200 4 5
# output : 205
# we need to find out the subsequence which should be in ascending order with maximum sum
# Python 3 solution

arr = list(map(int,input().split()))
mx = arr[0]; s = arr[0]
for i in range(1,len(arr)):
    if arr[i] > arr[i-1]: s += arr[i] # checking if subsequence is in ascending order, if yes we will continue to add it in sum.
    else: s = arr[i]   # if not we will break the subsequence from there and start a new subsequence
    if s > mx: mx = s  #we will check at each index if sum is greater than the sum of previous subsequence we will put that in mx 
print(mx)