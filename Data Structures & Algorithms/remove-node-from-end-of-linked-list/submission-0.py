class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        pos = length - n

        # removing the head
        if pos == 0:
            return head.next

        curr = head

        # move to node BEFORE the one we remove
        while pos > 1:
            pos -= 1
            curr = curr.next

        curr.next = curr.next.next

        return head