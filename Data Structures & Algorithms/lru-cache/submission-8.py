class Node:

    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.update(node)
            return node.val
        else:
            return -1

    def update(self, node: Node) -> None:
        # Remove the node from current pos
        prv, nxt = node.left, node.right
        prv.right = nxt
        nxt.left = prv

        # Push the node to top
        prv, nxt = self.head, self.head.right
        prv.right = node
        nxt.left = node
        node.left = prv
        node.right = nxt

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.update(node)
        else:
            if self.length == self.capacity:
                prv, node, nxt = self.tail.left.left, self.tail.left, self.tail
                del self.hash_map[node.key]
                prv.right = nxt
                nxt.left = prv
                self.length -= 1

            node = Node(key=key, val=value)
            prv, nxt = self.head, self.head.right
            prv.right = node
            nxt.left = node
            node.left = prv
            node.right = nxt
            self.hash_map[key] = node
            self.length += 1
