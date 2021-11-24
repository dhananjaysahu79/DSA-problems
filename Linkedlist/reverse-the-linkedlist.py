# Leetcode 206

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = prev = head
        while itr:
            nxt = itr.next
            itr.next = None if itr == head else prev
            prev = itr
            itr = nxt
        return prev