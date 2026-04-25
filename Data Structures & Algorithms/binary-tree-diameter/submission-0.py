class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def in_order(root):
            if not root:
                return 0
            
            left = in_order(root.left)
            right = in_order(root.right)
            total = left + right
            self.res = max(self.res, total)

            return 1 + max(left, right)
        
        in_order(root)
        return self.res