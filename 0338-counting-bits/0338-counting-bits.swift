class Solution {
    func countBits(_ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n + 1)
        for i in 0 ... n {
            ans[i] = ans[i/2] + i % 2
        }
        return ans
    }
}