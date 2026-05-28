# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):

            # If q (subroot) reach the end:
                # => All previous node in the path is same => True
            if not p and not q:
                return True

            # If q (subroot) not reach the end (not sastify the previous condition)
                # => And p already reach the end => False
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        res = False

        def dfs(root):
            if not root:
                return False
            
            if isSameTree(root, subRoot) == False:
                dfs(root.left)
                dfs(root.right)
            else:
                nonlocal res
                res = True
        dfs(root)
        return res

        