# 7.2.24
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


Solution().lengthOfLastWord("   fly me   to   the moon  ")
