class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # variable sliding window

        maxProfit = float("-inf")
        l = 0

        for r, num in enumerate(prices):
            maxProfit = max(maxProfit, num - prices[l])

            if num < prices[l]:
                # found a new low
                l = r

        return maxProfit

            

