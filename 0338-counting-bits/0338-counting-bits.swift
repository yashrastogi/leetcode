class Solution {
    func countBits(_ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n + 1)
        for i in 1 ..< n + 1 {
            ans[i] = ans[i/2] + i % 2
        }
        return ans
    }
}