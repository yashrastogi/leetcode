class Solution {
    func solveSudoku(_ matrix: inout [[Character]]) {
        func solve(_ r: Int = 0, _ c: Int = 0) -> Bool {
            var r = r, c = c
            while matrix[r][c] != "." {
                c += 1
                if c == 9 {
                    c = 0
                    r += 1
                    if r == 9 {
                        return true
                    }
                }
            }
            for i in 1 ... 9 {
                if isValid(r, c, i) {
                    matrix[r][c] = Character(String(i))
                    if !solve(r, c) {
                        matrix[r][c] = "."
                    } else {
                        return true
                    }
                }
            }
            return false
        }   
        func isValid(_ row: Int, _ col: Int, _ val: Int) -> Bool {
            guard row < 9 && col < 9 else { return false }
            // Each of the digits 1-9 must occur exactly once in each row.
            for r in 0 ..< 9 {
                if matrix[r][col] == Character(String(val)) {
                    return false
                }
            }
            // Each of the digits 1-9 must occur exactly once in each column.
            for c in 0 ..< 9 {
                if matrix[row][c] == Character(String(val)) {
                    return false
                }
            }
            // Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
            let boxRowStart = (row / 3) * 3
            let boxColStart = (col / 3) * 3
            let boxRowEnd = boxRowStart + 2
            let boxColEnd = boxColStart + 2
            for r in boxRowStart ... boxRowEnd {
                for c in boxColStart ... boxColEnd {
                    if matrix[r][c] == Character(String(val)) { return false }
                }
            }
            return true
        }
        solve()
    }
    
}