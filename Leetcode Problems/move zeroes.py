class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = b = 0
        while b < len(nums):
            if nums[b] != 0:
                if a != b: nums[b],nums[a] = nums[a],nums[b]
                a += 1
            b += 1