class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Variable window
        # Condition - if R is <= L (smallest seen so far), L = R
        # Update global variable with prices[r] - prices[l]

        l = 0

        result = 0

        for r, price in enumerate(prices):
            # ADD
            result = max(result, prices[r] - prices[l])

            # Shrink
            if prices[r] <= prices[l]:
                l = r

            # Record
            
        return result