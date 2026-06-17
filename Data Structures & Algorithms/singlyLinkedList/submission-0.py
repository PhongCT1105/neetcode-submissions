class ListNode:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(None, None)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = ListNode(val, None)
        
    def remove(self, index: int) -> bool:
        curr = self.head
        while curr.next and index > 0:
            curr = curr.next
            index -= 1

        if index == 0:
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        list_node = []
        curr = self.head.next
        while curr:
            list_node.append(curr.val)
            curr = curr.next

        return list_node
