from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


# The relative order means that in respect to the original order, the new partitioned set will maintain that ordering
# Non-Decreasing Order: This term refers to the way the elements in the array are sorted. In a non-decreasing order, each element in the array is less than or equal to the next element.
