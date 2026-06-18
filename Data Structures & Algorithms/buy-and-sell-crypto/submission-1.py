class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Variable window
        # What am I keep track of / valid()
            # keep track of lowest price seen using left pointer
        # What do I record and where do I store it?
            # global variable

        left = 0
        maxProfit = 0

        for right, price in enumerate(prices):
            if price <= prices[left]:
                left = right

            maxProfit = max(maxProfit, prices[right] - prices[left])

        return maxProfit

