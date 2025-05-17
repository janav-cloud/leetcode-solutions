class Solution(object):
    def romanToInt(self, s):
        symb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for ii, i in enumerate(s):
            res += symb[i]
            if ii + 1 != len(s) and symb[s[ii + 1]] > symb[s[ii]]:
                res -= 2 * symb[s[ii]]
        return res