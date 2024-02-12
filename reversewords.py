# 12.2.24
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
