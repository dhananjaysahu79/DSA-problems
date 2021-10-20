class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in nums2[::-1]:
            while len(stack) and i > stack[-1]: stack.pop()
            if len(stack): dic[i] = stack[-1]
            stack.append(i)

        ans = []
        for i in nums1:
            ans.append(dic.get(i,-1))
        return ans