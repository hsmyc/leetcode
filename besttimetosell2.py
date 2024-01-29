# 29.1.24
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


Solution().maxProfit([1, 5, 3, 3, 4, 6, 2, 3, 5, 1])
