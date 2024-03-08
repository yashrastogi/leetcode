class Solution {
    func robIterative(_ nums: [Int]) -> Int {
        guard nums.count > 1 else { return nums[0] }
        var dp = nums; dp[1] = max(nums[0], nums[1])
        for i in stride(from: 2, to: dp.count, by: 1) {
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        }
        return max(dp[dp.count - 1], dp[dp.count - 2])
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