public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;
        while (r < prices.Length) {
            int diff = prices[r] - prices[l];
            if (diff <= 0) {
                l = r;
                r += 1;
                continue;
            }
            if (diff > profit) {
                profit = diff;
            }
            r += 1;
        }
        return profit;
    }
}
