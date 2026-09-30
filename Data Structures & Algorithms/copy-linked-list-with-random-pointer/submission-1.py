"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a new copy linked list, new node with same value
        # Store the map of the old to new value for the pointer copy

        new_head = Node(x=0)
        new_curr = new_head
        old_to_new_map = {None:None}
        curr = head
        while curr:
            node = Node(x=curr.val)
            new_curr.next = node
            new_curr = new_curr.next
            old_to_new_map[curr] = new_curr 
            curr = curr.next

        new_curr = new_head.next
        curr = head

        while curr:
            new_curr.random = old_to_new_map[curr.random]
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head.next
        