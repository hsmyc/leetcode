# 21.1.24
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
