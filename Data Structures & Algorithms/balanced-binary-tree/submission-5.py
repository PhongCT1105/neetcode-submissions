# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Get height of both side: Compare the difference if it <= 1 => True else False

        def dfs(root):
            if not root:
                return (0, True)

            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left[0]-right[0]) <= 1 and left[1] is True and right[1] is True:
                return (max(left[0], right[0])+1, True)
            else:
                return (max(left[0], right[0])+1, False)

        res = dfs(root)

        return res[1]