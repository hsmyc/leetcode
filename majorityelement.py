# 26.1.24
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        print(nums[n//2])
        return nums[n//2]


Solution().majorityElement([2, 2, 1, 1, 1, 1, 2, 2])
