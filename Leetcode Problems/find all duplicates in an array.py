class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            curr = abs(nums[i]) - 1
            if nums[curr] < 0: ans.append(curr+1)
            else: nums[curr] = -nums[curr]
        return ans