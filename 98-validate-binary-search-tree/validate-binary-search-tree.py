# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize 'now' to a very small value
        self.now = float('-inf')

    def assign(self, n):
        # Check if the current node's value is greater than the previous value
        ret = self.now < n
        self.now = n
        return ret
    
    def isValidBST(self, root):
        if not root:
            return True
        
        # Perform in-order traversal
        return self.isValidBST(root.left) and self.assign(root.val) and self.isValidBST(root.right)