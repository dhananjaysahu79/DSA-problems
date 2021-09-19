# A naive approach is taking a set an keep the visited node
# O(n) space


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while True:
            if head == None: return False
            if head in s:
                return True
            s.add(head)
            head = head.next

# Better approach is taking slow and fast pointer.
# O(1) space.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head == None or head.next == None: return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == None or fast == None: return False
            if slow == fast:
                return True
        return False