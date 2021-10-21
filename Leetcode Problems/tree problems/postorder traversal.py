# Approach 1: Recursive approach | O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root: return
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)
        traverse(root)
        return ans

# What if interviewer tell you he dont want recursive approach?
#Approach 2: two stack approach (iterative) and reverse | O(n)
# In this approach we will traverse in root => right => left order
# then we will reverse it and we get our answer.

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans
        stack = [root]
        while len(stack):
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                ans.append(node.val)
        return ans[::-1]


# What if interviewer tell you that dont traverse in reverse order?
# Approach 3: one stack approach | O(2n)

