# Explaination:

# All the prices individually will follow the criteria, So we will start our answer with the length of the array.
# Now traverse the prices and find the length of the subarray that is strictly decreasing by 1unit ie (prices[i] - prices[i+1] == 1)
# When the above condition fails we simply calculate the number of subarray that can be formed with that length. We can use c * (c+1) // 2 formula to calculate the number of subarrays. But we have already included all the individuals at the start, so we have to remove individuals from the formula, So our resultant formula will be (c * (c+1)) // 2 - c
# when we traversed all the prices, we will again find the subarray, because their might be a subarray that was continously decreasing till the end.
# Hope I am able to explain it well

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        
        def count_subarrays(c):
            return (c * (c+1)) // 2 - c
            
        ans = n = len(prices)
        c = 1
        
        for i in range(n-1):
            if prices[i] - prices[i+1] == 1: c += 1
            else:
                ans += count_subarrays(c)
                c = 1
        ans += count_subarrays(c)
        
        return ans