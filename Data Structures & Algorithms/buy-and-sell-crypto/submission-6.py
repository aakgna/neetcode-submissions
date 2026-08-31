class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        prof = 0
        while j < len(prices):
            temp = prices[j] - prices[i]
            if temp > prof:
                prof = temp
                j += 1
                continue
            elif temp <= prof:
                j += 1
                if temp < 0:
                    i = j - 1
        return prof