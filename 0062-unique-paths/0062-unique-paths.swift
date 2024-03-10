class Solution {
    var memo = [[Int]]()

    func uniquePathsIterative(_ m: Int, _ n: Int) -> Int {
        for i in stride(from: m - 2, to: -1, by: -1) {
            for j in stride(from: n - 2, to: -1, by: -1) {
                memo[i][j] = memo[i + 1][j] + memo[i][j + 1]
            }
        }
        return memo[0][0]
    }

    func uniquePathsRecursive(_ m: Int, _ n: Int) -> Int {
        guard m >= 0 && n >= 0 else { return 0 }
        if m == 0 && n == 0 { return 1 }
        if memo[m][n] == 1 {
            memo[m][n] = uniquePathsRecursive(m - 1, n) + uniquePathsRecursive(m, n - 1)
        }
        return memo[m][n]
    }

    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        let recursive = false
        if recursive {
            memo = Array(repeating: Array(repeating: 1, count: n), count: m)
            return uniquePathsRecursive(m - 1, n - 1)
        } else {
            memo = Array(repeating: Array(repeating: 1, count: n), count: m)
            return uniquePathsIterative(m, n)
        }
    }
}
