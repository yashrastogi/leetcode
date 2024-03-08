class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
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
}
