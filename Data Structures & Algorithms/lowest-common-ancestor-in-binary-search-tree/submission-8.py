# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1 Larger and 1 smaller -> the curr root is the lowest ancestor:
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        # If current p or q equal to root -> it's the lowest by itself:
        if p.val == root.val or q.val == root.val:
            return root
        # Now both should be both larger or smaller:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        