class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var rows = [[1]]
        for i in 1..<numRows {
            var row = [1]
            for j in 0..<i - 1 {
                row.append(rows[i - 1][j] + rows[i - 1][j + 1])
            }
            row.append(1)
            rows.append(row)
        }
        return rows
    }
}
