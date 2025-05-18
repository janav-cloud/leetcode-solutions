class Solution:
    def dfs(self, row, col, vis, board):
        # Mark the current cell as visited
        vis[row][col] = True
        n, m = len(board), len(board[0])
        
        # Directions for traversing: down, up, left, right
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nrow, ncol = row + dr, col + dc
            # Check bounds, visitation, and if it's an 'O'
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and board[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, vis, board)
    
    def solve(self, board):
        n, m = len(board), len(board[0])
        # Visited matrix to track processed cells
        vis = [[False] * m for _ in range(n)]

        # Traverse border rows (first and last columns)
        for i in range(n):
            if not vis[i][0] and board[i][0] == 'O':
                self.dfs(i, 0, vis, board)
            if not vis[i][m - 1] and board[i][m - 1] == 'O':
                self.dfs(i, m - 1, vis, board)
        
        # Traverse border columns (first and last rows)
        for j in range(m):
            if not vis[0][j] and board[0][j] == 'O':
                self.dfs(0, j, vis, board)
            if not vis[n - 1][j] and board[n - 1][j] == 'O':
                self.dfs(n - 1, j, vis, board)
        
        # Flip unvisited 'O' to 'X', retain visited 'O' as is
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'