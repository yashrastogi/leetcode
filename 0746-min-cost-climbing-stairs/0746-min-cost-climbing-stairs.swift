class Solution {
    func minCostClimbingStairsIterative(_ cost: [Int]) -> Int {
        var dp = cost
        for i in stride(from: 2, to: cost.count, by: 1) {
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        }
        return min(dp[dp.count - 1], dp[dp.count - 2])
    }

    func minCostClimbingStairsRecursive(_ cost: [Int]) -> Int {
        var memo = Array(repeating: -1, count: cost.count)

        func recursion(_ i: Int) -> Int {
            guard i < cost.count else { return 0 }
            if memo[i] == -1 {
                memo[i] = cost[i] + min(recursion(i + 1), recursion(i + 2))
            }
            return memo[i]
        }

        return min(recursion(0), recursion(1))
    }

    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        return minCostClimbingStairsIterative(cost)
    }
}
