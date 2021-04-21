# find the duplicate number in the array of size n+1
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.
# Input: nums = [1,3,4,2,2]
# Output: 2


# O(n) solution
nums = list(map(int,input().split()))
arr = [0] * len(nums)  # taking arr with default value 0
for i in nums:
    if arr[i]:   # if value at particular i index af arr is 1 it means we have already saw that value before.
        print(i)
        break
    else: arr[i] = 1  # if we haven't saw that before we will mark as 1 as we saw that value now.



# O(n) , O(1) solution
# in this solution will jump to particular index and change its postion value to -1 and
# we will jump to another index with the value present at that index where we just put -1

nums = list(map(int,input().split()))
i = nums[0] # we will be storing the value of a particular index in i
while True:
    if nums[i] == -1: # if position value of that i is -1 it means we have already visited that index.
        print(i)
        break
    nums[i] , i = -1 , nums[i] # if not then we will put -1 at that position, and our next i would be the value at that index where we put that -1