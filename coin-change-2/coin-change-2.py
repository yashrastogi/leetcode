class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        l1, l2 = amt + 1, len(coins) + 1
        dp = [[-1] * l2 for _ in range(l1)]
        
        def bottomUp(dp, amount, coin):
            if amount == 0: return 1
            elif amount < 0 or coin == 0: return 0
            if (t := dp[amount][coin]) != -1: return t
            dp[amount][coin] = bottomUp(dp, amount - coins[coin - 1], coin) \
                                + bottomUp(dp, amount, coin - 1)
            return dp[amount][coin]
        
        return bottomUp(dp, amt, len(coins))