# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = TreeNode()
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val < root.val:
            return root
        if p.val < root.val and q.val > root.val:
            return root
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        if p.val > root.val and q.val > root.val:
            res = self.lowestCommonAncestor(root.right, p, q)
        else:
            res = self.lowestCommonAncestor(root.left, p, q)

        return res