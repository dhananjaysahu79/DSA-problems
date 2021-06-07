# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.


# A naive approach will be traversing each index and find the maximum element at the left subarary and
# maximum element at the right subarray. And then find the minimum of left maximum and right maximum and hence the water
# trapped at that paricular index would be height at that index minus the min out of it.
# that would be O(n^2)

# The same logic can be applied in optimised approach but we need to figure out how to find the maximum of the right size
# and to the left side in one go and not n times for a particular index.
# so we can use one array to store the maximum at particular index for left side. and maximum of the right side in another
# iteration. Space complexity would be O(n).

arr = list(map(int,input().split()))
n = len(arr)
if n < 3: print(0)
else:
    left_max = [0] * n
    mx = water = 0
    for i in range(0,n-1):
        mx = max(mx, arr[i])
        left_max[i] = mx
    right_max = arr[n-1]
    for i in range(n-2,0,-1):
        right_max = max(right_max, arr[i])
        water += min(right_max, left_max[i]) - arr[i]
    print(water)


# Now how to do it in O(1) space and also O(n) linear time.
# Using two pointer approach.

arr = list(map(int,input().split()))
n = len(arr)
left = 1; right = n - 2
left_max = arr[0]
right_max = arr[n-1]
water = 0

while left <= right:
    if left_max <= right_max:
        left_max = max(arr[left], left_max)
        water += left_max - arr[left]
        left += 1
    else:
        right_max = max(arr[right], right_max)
        water += right_max - arr[right]
        right -= 1
print(water)




