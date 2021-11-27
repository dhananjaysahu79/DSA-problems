# O(n) and O(1) space
# Also you need to solve it without using division operator.
# the array used for returning the answer is not considered as a space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        for i in range(n-2,-1,-1):
            ans[i] = nums[i+1] * ans[i+1]
            
        prefix_muls = 1
        for i in range(n):
            ans[i] *= prefix_muls
            prefix_muls *= nums[i]
        return ans