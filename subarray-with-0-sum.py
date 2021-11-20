# GeeksforGeeks easy

class Solution:
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        s = set()
        sm = 0
        for i in range(n):
            sm += arr[i]
            if sm == 0: return True
            if sm in s: return True
            s.add(sm)
        return False