# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append(None)
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(p)
        tree_1 = res
        res = []
        dfs(q)
        tree_2 = res
        print(tree_1, tree_2)
        return tree_1 == tree_2