# 30.1.24
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True


Solution().canJump([3, 2, 1, 0, 4])
Solution().canJump([2, 3, 1, 1, 4])

# The `enumerate` function takes an iterable as an argument (in this case `nums`) and returns an iterator that produces tuples.
# Each tuple contains two elements: the index of the current item and the current item itself.
