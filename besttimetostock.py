# 28.1.24
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            print(0)
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        print(max_profit)
        return max_profit


Solution().maxProfit([7, 2, 9, 1, 5, 3, 6, 4, 10])
Solution().maxProfit([7, 6, 4, 3, 1])
