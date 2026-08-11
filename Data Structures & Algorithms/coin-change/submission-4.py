class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            res = float("inf")
            for coin in coins:
                val = i - coin
                if val >= 0:
                    res = min(res, 1 + dp[val])

            dp[i] = res

        print(dp)

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]

