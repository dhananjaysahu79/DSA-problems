# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        q = [root]
        while len(q):
            temp = []
            for i in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(temp)
        return ans[::-1]