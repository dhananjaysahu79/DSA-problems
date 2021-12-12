# Leetcode 416 | Medium

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s,n = sum(nums), len(nums)
        if s & 1: return False
        
        dp = [[-1 for _ in range(s+1)]] * (n + 1)
        s = s // 2
     
        def traverse(sm, i):
            if sm == s: return 1
            if i >= n: return 0
            if dp[i+1][sm+nums[i]] == -1: 
                dp[i+1][sm+nums[i]] = traverse(sm+nums[i], i+1)
            if dp[i+1][sm] == -1:   
                dp[i+1][sm] = traverse(sm , i+1)         
            return dp[i+1][sm+nums[i]] or dp[i+1][sm]   
        return traverse(0,0)


# Approach 2: O(n * sum / 2)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       
        s,n = sum(nums), len(nums)
        if s & 1: return False
        s = s // 2
        dp = [[-1 for _ in range(s+1)]] * (n + 1)
        def traverse(sm, i):
            if sm == s: return 1
            if i >= n: return 0
            c1 = c2 = 0
            if sm+nums[i] <= s and dp[i+1][sm+nums[i]] == -1: 
                dp[i+1][sm+nums[i]] = traverse(sm+nums[i], i+1)
                c1 = dp[i+1][sm+nums[i]]
            if dp[i+1][sm] == -1:   
                dp[i+1][sm] = traverse(sm , i+1)  
                c2 = dp[i+1][sm]
            return c1 or c2  
        return traverse(0,0)