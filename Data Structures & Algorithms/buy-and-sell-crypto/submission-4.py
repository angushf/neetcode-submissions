class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Variable window
        
        profit = float("-inf")
        l = 0
        
        for r, price in enumerate(prices):
            profit = max(profit, price - prices[l])

            if price <= prices[l]:
                l = r

        return profit