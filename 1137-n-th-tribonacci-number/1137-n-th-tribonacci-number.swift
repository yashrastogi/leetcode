class Solution {
    var memo = [0: 0, 1: 1, 2: 1]

    func tribonacci(_ n: Int) -> Int {
        var dp = Array(repeating: 1, count: n + 1); dp[0] = 0
        for i in stride(from: 3, to: n + 1, by: 1) {
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        }
        return dp.last!
    }

    func recTribonacci(_ n: Int) -> Int {
        memo[n] = memo[n] ?? tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        return memo[n]!
    }
}
