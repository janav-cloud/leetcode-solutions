# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,s,stack):
        
        if not root.right and not root.left:
            stack.append(10*s+root.val)
            print(stack)
            return
        if root.left:
            self.dfs(root.left,s*10+root.val,stack)
        if root.right:
            self.dfs(root.right,s*10+root.val,stack)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        self.dfs(root,0,stack)
        
        return sum(stack)