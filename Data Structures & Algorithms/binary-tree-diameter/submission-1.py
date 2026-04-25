class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def in_order(root):
            nonlocal res            
            if not root:
                return 0
            left = in_order(root.left)
            right = in_order(root.right)
            total = left + right
            res = max(res, total)

            return 1 + max(left, right)
        
        in_order(root)
        return res