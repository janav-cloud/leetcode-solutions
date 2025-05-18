class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def backtrack(i,j,k):
            if len(s1) + len(s2) != len(s3):
                return False
            if i==len(s1) and j==len(s2):
                return True
            res = []
            if i<len(s1) and s1[i]==s3[k]:
                res.append(backtrack(i+1,j,k+1))
            if j<len(s2) and s2[j]==s3[k]:
                res.append(backtrack(i,j+1,k+1))
            return any(res)

        return backtrack(0,0,0)