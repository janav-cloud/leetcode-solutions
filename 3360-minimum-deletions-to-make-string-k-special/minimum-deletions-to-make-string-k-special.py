class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        table = {}
        for ch in word:
            if ch in table:
                table[ch] += 1
            else:
                table[ch] = 1

        d = float('inf')
        vals = list(table.values())

        for reference in vals:
            temp_d = 0
            for val in vals:
                if val < reference:
                    temp_d += val
                elif val > reference + k:
                    temp_d += val - (reference + k)
            d = min(d, temp_d)

        return d