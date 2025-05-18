# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traverse_lst = []
        violated_pairs = []
        prev = None

        """
        There are only two cases
        case 1:
            The violated pairs are adjacent to each other
            1 2 3 4 5 6 7
            1 3 2 4 5 6 7 (3 and 2)
            [(3,2)]
        
        case 2:
            The violated pairs are not adjacent to each other
            1 2 3 4 5 6 7
            1 6 3 4 5 2 7 (6 and 2)
            [(6,3), (5,2)]
        """
        def get_violated_pairs():
            node1, node2 = None, None
            if len(violated_pairs) == 1:
                node1, node2 = violated_pairs[0] # case 1
            else:
                node1, node2 = violated_pairs[0][0], violated_pairs[1][1] # case 2
            
            return node1, node2
                

        def inorder(node):
            nonlocal prev
            if node:
                inorder(node.left)
                if prev and node.val < prev.val:
                    violated_pairs.append((prev, node))
                traverse_lst.append(node.val)
                prev = node
                inorder(node.right)
        
        inorder(root)
        a, b  = get_violated_pairs()
        
        # swap values
        a.val, b.val = b.val, a.val

