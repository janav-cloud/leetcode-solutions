class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ' and i >= 0:
            count += 1
            i -= 1
        return count