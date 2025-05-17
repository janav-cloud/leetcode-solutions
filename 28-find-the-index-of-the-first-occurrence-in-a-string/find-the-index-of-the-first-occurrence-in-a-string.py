class Solution:
    def strStr(self, s: str, needle: str) -> int:
        l=0
        r=0
        while r<len(s):
            if r-l+1==len(needle):
                if s[l:r+1]==needle:
                    return l
                else:
                    l=l+1
            r=r+1
        return -1