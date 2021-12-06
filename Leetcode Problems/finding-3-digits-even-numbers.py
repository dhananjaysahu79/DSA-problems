# Leetcode: 2094 | Easy

class Solution:
    def findEvenNumbers(self, nums: List[int]) -> List[int]:
        
        def isEqual(num, H):
            F = [0] * 10
            while num > 0:
                F[num % 10] += 1
                num = num // 10
            for i in range(10):
                if F[i]:
                    if F[i] > H[i]: return False
            return True
                
        
        H = [0] * 10
        for i in nums: H[i] += 1
            
        ans = []
        for i in range(100,999,2):
            if isEqual(i, H): ans.append(i)
        return ans
            
            
                    
                        
                
        