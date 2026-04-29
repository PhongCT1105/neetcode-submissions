# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def dfs(node):
            if not node:
                return 0
            total_left = dfs(node.left)
            total_right = dfs(node.right)
            total_diameter = total_left + total_right
            nonlocal res
            res = max(res, total_diameter)

            return max(total_left, total_right) + 1
        
        dfs(root)
        return res
            

