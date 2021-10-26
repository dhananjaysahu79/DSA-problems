# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(root):
            if not root: return
            root.left, root.right = root.right, root.left
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return root
        