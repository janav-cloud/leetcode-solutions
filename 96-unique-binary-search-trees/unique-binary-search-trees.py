class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        
        def count_bsts(num_nodes: int) -> int:
            # Base case
            if num_nodes <= 1:
                return 1
            
            # If we've computed this before, use the cached result
            if num_nodes in memo:
                return memo[num_nodes]
            
            total = 0
            # Try each number from 1 to num_nodes as the root
            for root in range(1, num_nodes + 1):
                left_count = count_bsts(root - 1)
                right_count = count_bsts(num_nodes - root)
                total += left_count * right_count
            
            # Store in memo before returning
            memo[num_nodes] = total
            return total
        
        return count_bsts(n)