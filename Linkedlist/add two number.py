# leetcode linkedlist problem
# link = 'https://leetcode.com/problems/add-two-numbers/'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''; num2 = ''
        itr = l1
        while itr:
            num1 += str(itr.val)
            itr = itr.next
        itr = l2
        while itr:
            num2 += str(itr.val)
            itr = itr.next
        sm = str(int(num1[::-1]) + int(num2[::-1]))
        prev = l1
        for i in range(len(sm)-1,-1,-1):
            node = ListNode(int(sm[i]),None)
            if i == len(sm)-1:
                l1 = node
            prev.next = node
            prev = node
        return l1

