# Leetcode 2091 | Medium

# Python O(n) one pass solution

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi, mini, n = 0,0,len(nums)
        
        for i in range(n):
            if nums[i] < nums[mini]: mini = i
            if nums[i] > nums[maxi]: maxi = i
        i = min(mini,maxi)
        j = max(maxi,mini)
        return min(j+1, n-i , i+1+n-j)
        