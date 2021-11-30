# Leetcode: 2090 | Medium
# Approach 1: O(n) time using prefix sum

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        sm,left,rem,n = 0,0,0,len(nums)
        
        ans = [-1] * n
        for i in range(n-1,-1,-1):
            ans[i] = sm - rem
            if i < n -k: rem += nums[i+k]
            sm += nums[i]
            
        sm = 0
        for i in range(n):
            sm += nums[i]
            if i >= k and i < n-k:
                ans[i] = (sm+ans[i]-left) // (2*k+1)
                left += nums[i-k]
            else: ans[i] = -1
        return ans