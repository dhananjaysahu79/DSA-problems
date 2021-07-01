# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums
# being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#two pointers approach
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a,b = 0,1
        if len(nums) == 0: return 0
        while b < len(nums):
            if nums[b] != nums[a]:
                a += 1
                nums[a] = nums[b]
            b += 1
        return a + 1