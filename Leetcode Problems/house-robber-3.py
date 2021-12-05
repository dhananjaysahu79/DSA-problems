# Leetcode: 337 | Medium
# O(N) time and O(1) space

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:      
        maxi = 0
        def traverse(node):
            if not node: return [0,0]
            left = traverse(node.left)
            right = traverse(node.right)
            return [max(left) + max(right), node.val+left[0]+right[0]]
        return max(traverse(root))