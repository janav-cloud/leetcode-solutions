class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        total = m + n - 2
        k = min(m - 1, n - 1)
        ans = 1
       
        for i in range(1, k + 1):
            ans = ans * (total - k + i) // i

        return ans      