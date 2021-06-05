import pprint 

class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        l1, l2 = amt + 1, len(coins) + 1
        dp = [[0] * l2 for _ in range(l1)]
        
        def bottomUp(dp, amount, coin):
            if amount == 0: return 1
            elif amount < 0 or coin == 0: return 0
            if (t := dp[amount][coin]) != 0: return t
            dp[amount][coin] = bottomUp(dp, amount - coins[coin - 1], coin) \
                                + bottomUp(dp, amount, coin - 1)
            return dp[amount][coin]
        
        def topDown(dp, amount, coin):
            for i in range(amount + 1):
                for j in range(coin + 1):
                    if j == 0: dp[i][j] = 0
                    if i == 0: dp[i][j] = 1
            for i in range(1, amount + 1):
                for j in range(1, coin + 1):
                    if i - coins[j - 1] >= 0:
                        dp[i][j] = dp[i - coins[j - 1]][j] + dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
            return dp[amount][coin]
        
        def topDown2(dp, amount, coin):
            dp[0][coin] = 1
            for j in range(1, coin + 1):
                for i in range(coins[j - 1], amount + 1):
                    if i - coins[j - 1] >= 0:
                        dp[i][coin] = dp[i][coin] + dp[i - coins[j - 1]][coin]
            return dp[amount][coin]
        
        a = topDown2(dp, amt, len(coins))
        # pprint.pprint(dp)
        return a