# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = []
        def dfs(root):
            if not root:
                encode.append("N")
                return
            encode.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(encode)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        vals = data.split(",")
        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None

            node = TreeNode(val=int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

        