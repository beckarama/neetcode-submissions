class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0

        for R in range(1, len(prices)):
            profit = prices[R] - prices[L]

            max_profit = max(max_profit, profit)
            if prices[L] > prices[R]:
                L = R
        return max_profit