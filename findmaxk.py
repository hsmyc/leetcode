# 2.5.24
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        List.sort(nums)
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i]+nums[j] == 0:
                return nums[j]
            elif nums[i]+nums[j] > 0:
                j -= 1
            else:
                i += 1
        return -1
