# Leetcode 1306 : Medium

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        self.ans,n = False,len(arr)
        visited = [0] * n
        
        def traverse(i):
            if i < 0 or i >= n or visited[i]: return 
            if arr[i] == 0: 
                self.ans = True
                return
            visited[i] = 1
            traverse(i-arr[i])
            traverse(i+arr[i])
        traverse(start)
        
        return self.ans
        