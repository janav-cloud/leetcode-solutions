class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        ans = 0
        if len(haystack) < len(needle):
            return -1
        if needle == "":
            return 0
        while i < (len(haystack) - len(needle) + 1):
            if haystack[i+j] == needle[j]:
                if j == len(needle) - 1:
                    return i
                j += 1
            else:
                i += 1
                j = 0
        return -1