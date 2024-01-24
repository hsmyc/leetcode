from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i+2]:
                del nums[i]
            else:
                i += 1
        print(nums)
        return len(nums)


Solution().removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3])
