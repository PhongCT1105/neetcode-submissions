class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS recursive
        res = 0
        def post_order(root):
            nonlocal res            
            if not root:
                return 0
            left = post_order(root.left)
            right = post_order(root.right)
            total = left + right
            res = max(res, total)

            return 1 + max(left, right)
        
        post_order(root)
        return res