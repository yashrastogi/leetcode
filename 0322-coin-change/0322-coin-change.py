class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def topDown():
            memo = {}

            def rec(d):
                if d == 0:
                    return 0
                elif d < 0:
                    return float("inf")
                elif d in memo:
                    return memo[d]
                ret = float("inf")
                for de in coins:
                    ret = min(ret, 1 + rec(d - de))
                memo[d] = ret
                return ret

            r = rec(amount)
            if r == float("inf"):
                return -1
            return r

        def bottomUp():
            dp = [float("inf")] * (amount + 1)
            dp[0] = 0
            for i in range(1, len(dp)):
                for coin in coins:
                    if coin <= i:
                        dp[i] = min(dp[i], 1 + dp[i - coin])
            r = dp[amount]
            if r == float("inf"):
                return -1
            return r

        return bottomUp()
