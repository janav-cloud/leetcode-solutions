# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return ans
        stack=[(root,False)]
        
        while stack:
            node,vis=stack.pop()
            if node:
                if vis:
                    ans.append(node.val)
                else:
                    stack.append((node.right,False))
                    stack.append((node,True))
                    stack.append((node.left,False))
        return ans

        