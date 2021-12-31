class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def traverse(itr,currMax,currMin):
            if not itr: return
            
            self.ans = max(self.ans,itr.val - currMin, currMax - itr.val)
            currMax = max(currMax, itr.val)
            currMin = min(currMin, itr.val)
            
            traverse(itr.left, currMax, currMin)
            traverse(itr.right, currMax, currMin)
            
        traverse(root, root.val, root.val)
        
        return self.ans