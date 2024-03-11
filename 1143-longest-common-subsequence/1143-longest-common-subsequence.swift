class Solution {
    var dp = [[Int]]()

    private func iterative(_ text1: [Character], _ text2: [Character]) -> Int {
        var flag = false
        for i in stride(from: 0, to: text1.count, by: 1) {
            if text1[0] == text2[0] || text1[i] == text2[0] { flag = true }
            if flag { dp[i][0] = 1 }
        }
        flag = false
        for j in stride(from: 0, to: text2.count, by: 1) {
            if text1[0] == text2[0] || text1[0] == text2[j] { flag = true }
            if flag { dp[0][j] = 1 }
        }
        for i in stride(from: 1, to: text1.count, by: 1) {
            for j in stride(from: 1, to: text2.count, by: 1) {
                if text1[i] == text2[j] {
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                }
            }
        }
        return dp[text1.count - 1][text2.count - 1]
    }

    private func recursive(_ text1: [Character], _ text2: [Character], _ i: Int = 0, _ j: Int = 0) -> Int {
        guard i < text1.count && j < text2.count else { return 0 }
        if dp[i][j] == -1 {
            if text1[i] == text2[j] {
                dp[i][j] = 1 + recursive(text1, text2, i + 1, j + 1)
            } else {
                dp[i][j] = max(recursive(text1, text2, i + 1, j), recursive(text1, text2, i, j + 1))
            }
        }
        return dp[i][j]
    }

    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        let useRecursion = true
        var ans = 0
        if useRecursion {
            dp = Array(repeating: Array(repeating: -1, count: text2.count), count: text1.count)
            ans = recursive(Array(text1), Array(text2))
        } else {
            dp = Array(repeating: Array(repeating: 0, count: text2.count), count: text1.count)
            ans = iterative(Array(text1), Array(text2))
        }
        return ans
    }
}