# Leetcode: 2071 | Hard

class Solution:
    def maxTaskAssign(self, T: List[int], W: List[int], pills: int, strength: int) -> int:
        
        
        def isPossible(T,W,pills,strength):

            harderTask, strongestMan = len(T) - 1, -1
            
            for _ in range(len(T)):
                if W[strongestMan] >= T[harderTask]:
                    W.pop()
                else:
                    if not pills: return False
                    power_needed = T[harderTask] - strength
                    index = bisect.bisect_left(W,power_needed)
                    if index >= len(W): return False
                    pills -= 1
                    W.pop(index)
                harderTask -= 1
                
            return True
        
        
                    
        T.sort()
        W.sort()
        
        l,h, = 0, min(len(T),len(W))
        
        while l <= h:
            mid = (l+h) // 2

            res = isPossible(T[:mid], W[len(W)-mid:], pills, strength) 
            
            if res: l = mid + 1
            else: h = mid - 1
                
        return h
            
            
            
        
            
        
        
        
        
        
            
        