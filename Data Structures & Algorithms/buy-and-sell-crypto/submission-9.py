class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            diff = prices[r] - prices[l]
            if profit < diff:
                profit = diff
            r += 1
        return profit