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

        def dfs(node: TreeNode) -> bool:
            if not node:
                return (0, True)
            
            left = dfs(node.left)
            right = dfs(node.right)
            balance_degree = abs(left[0] - right[0])

            if balance_degree <= 1 and balance_degree >= 0 and left[1] == True and right[1] == True:
                return (max(left[0], right[0]) + 1, True) 
            else:
                return (max(left[0], right[0]) + 1, False)         
         
        return dfs(root)[1]