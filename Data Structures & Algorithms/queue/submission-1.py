class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.head = ListNode(None, None, None)
        self.tail = ListNode(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node, prev, next = ListNode(value), self.tail.prev, self.tail
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node

    def appendleft(self, value: int) -> None:
        node, prev, next = ListNode(value), self.head, self.head.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

    def pop(self) -> int:
        node = self.tail.prev
        if node != self.head:
            val = node.val
            prev = node.prev
            prev.next = self.tail
            self.tail.prev = prev
            return val

        return -1

    def popleft(self) -> int:
        node = self.head.next
        if node != self.tail:
            val = node.val
            next = node.next
            next.prev = self.head
            self.head.next = next
            return val

        return -1
