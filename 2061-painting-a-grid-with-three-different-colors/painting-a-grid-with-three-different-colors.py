MOD = 1_000_000_007

class Solution:
    def get_colors(self, config: int, m: int) -> list[int]:
        """Convert configuration number to list of colors."""
        colors = []
        for _ in range(m):
            colors.append(config % 3)
            config //= 3
        return colors
    
    def is_valid_config(self, colors: list[int]) -> bool:
        """Check if a column configuration is valid (no adjacent rows same color)."""
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                return False
        return True
    
    def is_compatible(self, prev: list[int], curr: list[int]) -> bool:
        """Check if two configurations are compatible (corresponding rows different colors)."""
        return all(p != c for p, c in zip(prev, curr))
    
    def colorTheGrid(self, m: int, n: int) -> int:
        # Step 1: Generate all possible configurations
        max_config = 3 ** m
        
        # Step 2: Identify valid configurations
        valid_configs = []
        for config in range(max_config):
            colors = self.get_colors(config, m)
            if self.is_valid_config(colors):
                valid_configs.append(config)
        
        # Step 3: Precompute valid transitions
        transitions = {curr: [] for curr in valid_configs}
        for curr in valid_configs:
            curr_colors = self.get_colors(curr, m)
            for prev in valid_configs:
                prev_colors = self.get_colors(prev, m)
                if self.is_compatible(prev_colors, curr_colors):
                    transitions[curr].append(prev)
        
        # Step 4: Initialize DP array
        dp = {config: 1 for config in valid_configs}  # First column: 1 way per valid config
        
        # Step 5: Process each column
        for _ in range(1, n):
            new_dp = {config: 0 for config in valid_configs}
            for curr in valid_configs:
                # Sum ways from all valid previous configurations
                new_dp[curr] = sum(dp[prev] for prev in transitions[curr]) % MOD
            dp = new_dp
        
        # Step 6: Sum ways for all valid configurations in last column
        return sum(dp[config] for config in valid_configs) % MOD