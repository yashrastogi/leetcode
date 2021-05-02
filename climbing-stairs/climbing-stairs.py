def rec(curr, n, memo):
    if curr == n:
        return 1
    elif curr > n:
        return 0
    if memo[curr] != -1:
        return memo[curr]
    memo[curr] = rec(curr + 1, n, memo) + rec(curr + 2, n, memo)
    return memo[curr]

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n
        return rec(0, n, memo)
        