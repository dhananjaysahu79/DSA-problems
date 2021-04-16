# KADANE'S ALGORITHM
# Maximum sum contigious subarray
#Python 3 solution

arr = list(map(int,input().split()))
s = 0 #variable to calculate at each index
curr_max = arr[0] #variable to store maximum at each index
for i in arr:
    s += i
    if s > curr_max: curr_max = s  # at any index if sum is greater than the current maximum we will update it to curr_max.
    if s < 1: s = 0 # if at any index sum is lesser than 1 we have to leave that subsequence,if not it will reduce the sum in further subsequence.
print(curr_max)

