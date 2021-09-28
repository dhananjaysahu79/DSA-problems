# In one sweep we will find the lowest among the right side of a particular index
# and store it in right array.
# logic: Think about it if an element in a particular index is lesser than the
# minimum element at its right side, So can I say that it is smaller than all the elements
# present in its right side?
# yes it is
# Similarly in the second sweep starting from the left we can find the maximum of the
# left side of particular index and we can say that if an element is greater than
# maximum present at its left side, so it is greater than all the elements present at its left. right

# O(n) time

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        right = [nums[-1]] * n
        for i in range(n-2,0,-1):
            right[i] = min(nums[i+1], right[i+1])

        maxi = nums[0]
        sm = 0
        for i in range(1,n-1):
            if nums[i] < right[i] and nums[i] > maxi:
                sm += 2
            elif nums[i] < nums[i+1] and nums[i] > nums[i-1]:
                sm += 1
            maxi = max(maxi,nums[i])
        return sm