# a naive approach is to find the length of the linkedlist and then find the median + 1
# Time complexity: O(n + n //2)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        c = 0
        while itr:
            c += 1
            itr = itr.next
        mid = c // 2 + 1
        itr = head
        for _ in range(mid-1): itr = itr.next
        return itr


# optimal solution is O(n) using fast and slow pointers
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast.next else slow