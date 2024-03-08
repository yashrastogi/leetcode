class Solution {
    func rob(_ nums: [Int]) -> Int {
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
}