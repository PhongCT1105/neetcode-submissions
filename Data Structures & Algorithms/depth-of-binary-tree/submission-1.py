# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res

            total_l = dfs(node.left)
            total_r = dfs(node.right)
            total = total_l + total_r
            res = max(total, res)
            return max(total_l, total_r) + 1

        dfs(root)
        return res