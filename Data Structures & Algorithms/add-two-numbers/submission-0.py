# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_1 = l1
        curr_2 = l2
        head = ListNode()
        curr_3 = head
        reminder = 0

        while curr_1 and curr_2:
            val = curr_1.val + curr_2.val + reminder
            if val < 10:
                reminder = 0
            else:
                reminder = 1
            curr_3.val = val%10 
            
            curr_1 = curr_1.next
            curr_2 = curr_2.next
            if curr_1 or curr_2:         
                curr_3.next = ListNode()
                curr_3 = curr_3.next

        while curr_1:
            val = curr_1.val + reminder
            if val < 10:
                reminder = 0
            else:
                reminder = 1
            curr_3.val = val%10
            curr_1 = curr_1.next
            if curr_1:                     
                curr_3.next = ListNode()
                curr_3 = curr_3.next

        while curr_2:
            val = curr_2.val + reminder
            if val < 10:
                reminder = 0
            else:
                reminder = 1
            curr_3.val = val%10
            curr_2 = curr_2.next
            if curr_2:                     
                curr_3.next = ListNode()
                curr_3 = curr_3.next
        if reminder:                  
            curr_3.next = ListNode(reminder)
        return head