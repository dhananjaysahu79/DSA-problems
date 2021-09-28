# O(1) space using two [pointers]

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        a = 0; b = 1
        while a < len(nums) and b < len(nums):
            if not nums[a] & 1: a += 2
            elif nums[b] & 1: b += 2
            else:
                nums[a],nums[b] = nums[b],nums[a]
                a += 2
                b += 2
        return nums
