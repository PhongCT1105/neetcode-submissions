# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Each subtree has to be balance
        # Balance = depth left is +-1 to depth right
        # Get depth

        def dfs(root: [TreeNode]) -> tuple(bool, int):
            if not root:
                return (True, 0)

            left = dfs(root.left)
            right = dfs(root.right)
            height = max(left[1], right[1]) + 1

            if left[0] == False or right[0] == False:
                return (False, height)
            elif abs(left[1] - right[1]) <= 1:
                return (True, height)
            else:
                return (False, height)

        res = dfs(root)

        return res[0]            
        
        