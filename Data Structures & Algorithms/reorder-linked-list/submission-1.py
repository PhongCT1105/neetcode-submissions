# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        curr = head
        # Find the middle first, use sp, fp:
        sp, fp = head, head
        while fp and fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next

        # Reverse the last half (sp+1 -> fp)
        curr = sp.next
        sp.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Concat both half together in order (List 1: head, List 2: prev)
        dummy_head = ListNode()
        curr1 = head
        curr2 = prev
        curr3 = dummy_head

        while curr1 and curr2:
            curr3.next = curr1
            curr3 = curr3.next
            curr1 = curr1.next
            curr3.next = curr2
            curr3 = curr3.next
            curr2 = curr2.next
        if curr1:
            curr3.next = curr1
        
