class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')
        
        def maxPath(node):
            if not node:
                return 0
            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))
            self.maxi = max(self.maxi, left + right + node.val)
            return node.val + max(left, right)
        
        maxPath(root)
        return self.maxi