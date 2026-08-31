class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]
        i, j = 0, 1
        while j < len(prices):
            profit_factor = prices[j] - prices[i]
            if profit_factor <= 0:
                i = j
                j = i + 1
                continue

            if profit_factor > max_profit:
                max_profit = profit_factor
            j += 1
        return max_profit