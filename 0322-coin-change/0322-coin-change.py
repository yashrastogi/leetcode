class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
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
