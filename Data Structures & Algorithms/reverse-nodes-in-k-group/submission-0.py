# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        # How many group of k nodes should be reversed, skip if exceed
        curr_group = 1
        total_group = cnt // k
        curr = head
        end = None

        while curr_group <= total_group:
            cnt = k
            start = curr
            prev = None

            while cnt > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt -= 1

            if end:
                end.next = prev   # add this

            # Curr, next move to the next part of the group
            # Prev now the cut point so after reveresed it become the end
            start.next = curr

            if curr_group == 1:
                dummy_head = prev 

            curr_group += 1
            end = start

        return dummy_head