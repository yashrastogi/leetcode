class Solution {
    func numTilings(_ n: Int) -> Int {
        var dp = [1, 2, 5, -1]
        for _ in stride(from: 3, to: n, by: 1) {
            dp[3] = (2 * dp[2] + dp[0]) % (Int(pow(10.0, 9.0)) + 7)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[3]
        }
        return dp[min(n - 1, 3)]
    }
}
