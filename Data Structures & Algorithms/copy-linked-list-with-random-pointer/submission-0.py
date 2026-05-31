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
        
        """
        Problem:
        - Copy only the chain value: O(N)
        - Copy the random also: O(N)

        For copy the random node:
        - When we build the copy only chain value
        => We built a dictionary that translate the old node to new node:
            e.g: old 3 -> new 3
        So when create random:
            - old 3 random -> old 5 random
            - get new 5 random through dictionary
            - connect new 3 with new 5
        """

        hash_map = {None: None}
        head_new = Node(0)
        curr, curr_new = head, head_new

        # Pass 1: Built hash map and value for deep copy O(N)
        while curr:
            node_copy = Node(curr.val)
            curr_new.next = node_copy
            curr_new = curr_new.next
            hash_map[curr] = curr_new
            curr = curr.next

        # Pass 2: Create random
        curr, curr_new = head, head_new.next
        while curr:
            print(curr.random)
            curr_new.random = hash_map[curr.random]
            curr_new = curr_new.next
            curr = curr.next
        
        return head_new.next