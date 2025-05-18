class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        filtered_words = [word for word in words if word]
        reversed_words = filtered_words[::-1]
        return ' '.join(reversed_words)