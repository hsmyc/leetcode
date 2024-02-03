# 3.2.24
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        return [left[i] * right[i] for i in range(n)]


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([1, 5, 3, 3, 4, 6, 2, 3, 5, 1]))
