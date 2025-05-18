class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                for left_tree in dp[root - 1]:
                    for right_tree in dp[nodes - root]:
                        root_node = TreeNode(root)
                        root_node.left = left_tree
                        root_node.right = self.clone(right_tree, root)
                        dp[nodes].append(root_node)
        return dp[n]
    
    def clone(self, n: TreeNode, offset: int) -> TreeNode:
        if n:
            node = TreeNode(n.val + offset)
            node.left = self.clone(n.left, offset)
            node.right = self.clone(n.right, offset)
            return node
        return None