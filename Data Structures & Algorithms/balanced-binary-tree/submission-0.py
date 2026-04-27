# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def post_order(node):
            if not node:
                return (True, 0)
            total_left = post_order(node.left)
            total_right = post_order(node.right)
            if total_left[1] - total_right[1] >= -1 and total_left[1] - total_right[1] <= 1:
                return (True, max(total_left[1], total_right[1]) + 1)
            else:
                return (False, max(total_left[1], total_right[1]) + 1)

        res = post_order(root)
        return res[0]

