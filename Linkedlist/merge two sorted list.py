class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1; b = l2
        head = None
        while a and b:
            min_node = a
            if a.val <= b.val: a = a.next
            else:
                min_node = b
                b = b.next
            if head == None: head = min_node
            else: prev.next = min_node
            prev = min_node
        while a:
            if head == None: head = a
            else: prev.next = a
            prev = a
            a = a.next
        while b:
            if head == None: head = b
            else: prev.next = b
            prev = b
            b = b.next
        return head