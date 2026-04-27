class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def post_order(node):
            if not node:
                return 0
            nonlocal res
            total_left = post_order(node.left)
            total_right = post_order(node.right)
            res = max(res, total_left + total_right)
            return 1 + max(total_left, total_right)

        post_order(root)
        return res  