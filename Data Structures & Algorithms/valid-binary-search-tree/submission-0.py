# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        from collections import deque 

        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                if node.left.val >= node.val:
                    return False
                q.append(node.left)

            if node.right:
                if node.right.val <= node.val:
                    return False
                q.append(node.right)
        
        return True