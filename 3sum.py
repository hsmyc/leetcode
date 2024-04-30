# 30.4.24
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The input list nums is sorted in ascending order. Sorting is crucial because it allows the subsequent two-pointer technique to be applied effectively.
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Two pointers l(left) and r(right) are initialized. l starts right after i and r starts from the end of the list. These pointers help in finding two additional numbers that, along with nums[i], sum up to zero.
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
