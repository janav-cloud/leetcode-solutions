class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words[0])
        m = len(words)*k
        if m > n: return []

        from collections import Counter
        wordsHash = Counter(words)
        
        # define a function to return all indices with offset i
        def slide_window_with_offset(i):
            loc_ans, seen, left = [], Counter(), offset
            for right in range(offset, n - k + 1, k):
                sub = s[right:right + k]
                if sub not in wordsHash:
                    seen.clear()
                    left = right + k # we move the left pointer
                else:
                    seen[sub] += 1
                    # shrink from left if a word is found to be over-used (iteratively until not)
                    while seen[sub] > wordsHash[sub]:
                        seen[s[left:left + k]] -= 1
                        left += k
                    # record if matched 
                    ## (length matching is good enough, since no wordsHash violation so far)
                    if right - left + k == m:
                        loc_ans.append(left)
                    # once done we keep expanding the right pointer for the next sub
            return loc_ans

        # for the final answer
        ans = []
        for offset in range(k):
            # for all possible offset (k of them in total)
            ans += slide_window_with_offset(offset)
        return ans