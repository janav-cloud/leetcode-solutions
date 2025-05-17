class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        prev = [j for j in range(n2 + 1)]
        curr = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            curr[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insertion = 1 + curr[j - 1]
                    deletion = 1 + prev[j]
                    replacement = 1 + prev[j - 1]
                    curr[j] = min(insertion, deletion, replacement)
            prev = curr[:]
        
        return prev[n2]