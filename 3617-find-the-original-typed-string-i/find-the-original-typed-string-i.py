class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ways = n
        for i in range(1,n):
            if word[i] != word[i-1]:
                ways -= 1
        return ways