# Leetcode 563 | Easy

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sm = 0
        if not root: return 0
        
        def traverse(node):
            if not node: return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.sm += abs(left - right)
            return left + right + node.val
        traverse(root)

        return self.sm