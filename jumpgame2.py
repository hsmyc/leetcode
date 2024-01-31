# 31.1.24
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        jumps = 0
        end = 0
        for i, j in enumerate(nums):
            if i > end:
                end = max_reach
                jumps += 1
            max_reach = max(max_reach, i + j)
        return jumps


Solution().jump([2, 3, 1, 1, 4])
