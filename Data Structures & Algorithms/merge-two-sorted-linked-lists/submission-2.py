# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        if not list1 and not list2:
            return dummy_head

        curr1, curr2 = list1, list2
        curr_merge = dummy_head

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr_merge.next = curr1
                curr1 = curr1.next
                curr_merge = curr_merge.next
            else:
                curr_merge.next = curr2
                curr2 = curr2.next
                curr_merge = curr_merge.next

        while curr1:
            curr_merge.next = curr1
            curr1 = curr1.next
            curr_merge = curr_merge.next

        while curr2:
            curr_merge.next = curr2
            curr2 = curr2.next
            curr_merge = curr_merge.next

        return dummy_head.next
