# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        qu = deque([])
        qu.append(root)
        res = []
        while qu:
            temp = []
            for _ in range(len(qu)):
                node = qu.popleft()
                temp.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(temp)
        return res[::-1]