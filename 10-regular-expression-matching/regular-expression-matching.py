class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # starting from the ends of the strings
        return self.match(s, p, len(s) - 1, len(p) - 1)

    def match(self, s: str, p: str, i: int, j: int) -> bool:
        # we reached the beginnings of both strings => they are mapped completely
        if i == -1 and j == -1:
            return True

        elif i >= 0 and j >= 0:
            # take current characters for string and pattern
            cS = s[i]
            cP = p[j]

            # cases (3.1) and (3.2)
            if cP != '*':
                return (cP == '.' or cP == cS) and self.match(s, p, i - 1, j - 1)
            else:
                # case (3.3) - need to find previous character from p
                prevP = p[j - 1]
                # case for * with 0 occurrences
                if prevP != '.' and prevP != cS:
                    return self.match(s, p, i, j - 2)
                # case for * with 1 or multiple occurrences (can be 0 too!)
                else:
                    return (self.match(s, p, i - 1, j - 2) or
                            self.match(s, p, i - 1, j) or
                            self.match(s, p, i, j - 2))

        # case which is explained in (4)
        elif i == -1:
            cP = p[j]
            if cP == '*':
                return self.match(s, p, i, j - 2)

        # all the cases when strings are not able to be matched
        return False