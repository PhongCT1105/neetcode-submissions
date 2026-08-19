# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1, list2
        dummy_res = ListNode()
        curr3 = dummy_res

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
                curr3 = curr3.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
                curr3 = curr3.next

        if curr1:
            curr3.next = curr1
            curr1 = curr1.next
            curr3 = curr3.next
        if curr2:
            curr3.next = curr2
            curr2 = curr2.next
            curr3 = curr3.next

        return dummy_res.next