class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = maxi = 0
        for i in nums:
            if i == 0: c = 0
            else: c += 1
            maxi = max(maxi, c)
        return maxi