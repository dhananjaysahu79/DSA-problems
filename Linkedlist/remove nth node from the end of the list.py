# A naive approach would be travering the end of the list and find its length and then again
# traverse that node which we want to delete.
# Time complexity : O(length + n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            length += 1
        length = (length + 1) * 2
        length -= 0 if fast.next else 1
        prev = itr = head
        for i in range(length- n + 1):
            if i == length - n:
                if itr == head: head = head.next
                if itr.next:
                    prev.next = itr.next
                else: prev.next = None
            prev = itr
            itr = itr.next
        return head


# Optimal approach would be O(length) linear time\
# by using two pointers

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = slow = head
        for _ in range(n): fast = fast.next

        if fast == None: return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head