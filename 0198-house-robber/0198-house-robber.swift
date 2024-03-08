class Solution {
    func robIterative(_ nums: [Int]) -> Int {
        var dp = nums
        for i in stride(from: 2, to: nums.count, by: 1) {
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        }
        return dp.last!
    }

    func robRecursive(_ nums: [Int]) -> Int {
        var memo = Array(repeating: -1, count: nums.count)
        func recursion(_ i: Int) -> Int {
            guard i < nums.count else { return 0 }
            if memo[i] == -1 {
                memo[i] = max(recursion(i + 2) + nums[i], recursion(i + 1))
            }
            return memo[i]
        }
        return recursion(0)
    }

    func rob(_ nums: [Int]) -> Int {
        return robIterative(nums)
    }
}
