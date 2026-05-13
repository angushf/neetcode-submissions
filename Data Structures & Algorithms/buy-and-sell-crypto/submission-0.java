class Solution {
    public int maxProfit(int[] prices) {
        // Initialize a left and right pointer
        int l = 0;
        int r = 1;
        int maxCount = 0;

        // Iterate over prices array while right pointer < length of prices
        // if prices[r] < prices[l], advance l ptr to r position
        // always advance r ptr
        while (r < prices.length) {
            int profit = prices[r] - prices[l];
            maxCount = Math.max(maxCount, profit);

            if (prices[r] < prices[l]) {
                l = r;
            }

            r++;
        }

        return maxCount;
    }
}
