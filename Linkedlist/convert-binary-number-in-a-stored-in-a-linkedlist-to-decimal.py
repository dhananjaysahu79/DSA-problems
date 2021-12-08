# Leetcode 1290 | Easy
# O(n) one pass, fastest solution

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        itr,num = head,0
        
        while itr:
            num = num * 2 + itr.val
            itr = itr.next
        return num