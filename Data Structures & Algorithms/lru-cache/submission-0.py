class Node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            # Ask if get key also update this as last use in cache to update
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = Node(val=val)
        prv, nxt = self.head, self.head.right
        prv.right = Node
        nxt.left = Node
        node.left = prv
        node.right = nxt
        
         
        
