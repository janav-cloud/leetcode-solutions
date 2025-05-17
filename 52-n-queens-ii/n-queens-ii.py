class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()    # Columns where queens are placed
        p = set()      # Positive diagonals (r+c) occupied by queens
        neg = set()    # Negative diagonals (r-c) occupied by queens
        res = 0        # Result counter
        board = [["."] * n for i in range(n)]  # Board representation
        
        def bt(r):
            nonlocal res 
            if r == n:  # Successfully placed queens in all rows
                res += 1
                return

            for c in range(n):
                # Check if current position conflicts with any queen
                if c in col or (r+c) in p or (r-c) in neg:
                    continue
                
                # Place queen and update constraints
                col.add(c)
                p.add(r+c)
                neg.add(r-c)
                board[r][c] = 'Q'

                # Recurse to next row
                bt(r+1)

                # Backtrack: remove queen and constraints
                col.remove(c)
                p.remove(r+c)
                neg.remove(r-c)
                board[r][c] = '.'
            
        bt(0)  # Start backtracking from row 0
        return res