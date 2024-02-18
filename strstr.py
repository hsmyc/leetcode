# 18.2.24
class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1


Solution().strStr("hello", "ll")
Solution().strStr("aaaaa", "bba")
