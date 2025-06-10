class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = -1
        min_even = float('inf')
        table = {}
        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1

        for value in table.values():
            if value % 2 == 0:
                if value < min_even:
                    min_even = value
            else:
                if value > max_odd:
                    max_odd = value

        return max_odd - min_even