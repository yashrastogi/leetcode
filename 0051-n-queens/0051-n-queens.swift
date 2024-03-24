class Solution {
    func solveNQueens(_ n: Int) -> [[String]] {
        func backtrack(_ i: Int = 0) {
            guard i < matrix.count else {
                ret.append(matrix.map { $0.joined() })
                return
            }
            for y in 0..<matrix[0].count {
                if !checkClash(i, y, matrix) {
                    matrix[i][y] = "Q"
                    backtrack(i + 1)
                    matrix[i][y] = "."
                }
            }
        }
        var matrix = Array(repeating: Array(repeating: ".", count: n), count: n)
        var ret = [[String]]()
        backtrack()
        return ret
    }

    func checkClash(_ i: Int, _ j: Int, _ matrix: [[String]]) -> Bool {
        guard i >= 0 && j >= 0 else { return false }
        // Check for other queens in the same row or column
        for x in 0..<matrix.count {
            if x != i && matrix[x][j] == "Q" {
                return true
            }
        }

        for y in 0..<matrix[0].count {
            if y != j && matrix[i][y] == "Q" {
                return true
            }
        }

        // Check diagonally
        for direction in [(1, 1), (-1, 1), (1, -1), (-1, -1)] {
            var x = i + direction.0
            var y = j + direction.1

            while x >= 0 && x < matrix.count && y >= 0 && y < matrix[0].count {
                if matrix[x][y] == "Q" {
                    return true
                }
                x += direction.0
                y += direction.1
            }
        }

        return false
    }

}