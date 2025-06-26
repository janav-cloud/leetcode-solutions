class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = 0
        ones = 0
        value = 0

        for ch in s:
            if ch == '0':
                zeros += 1

        binary = len(s) - 1
        power = 0

        while binary >= 0:
            if s[binary] == '1':
                if power >= 32:
                    break  # Prevents overflow beyond 2^31
                if value + 2**power <= k:
                    value += 2**power
                    ones += 1
            else:
                pass
            power += 1
            binary -= 1

        return ones + zeros