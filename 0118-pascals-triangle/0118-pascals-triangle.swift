class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var rows = [[1]]
        for i in stride(from: 2, to: numRows + 1, by: 1) {
            var row = [1]
            for j in stride(from: 0, to: i - 2, by: 1) {
                row.append(rows[i - 2][j] + rows[i - 2][j + 1])
            }
            row.append(1)
            rows.append(row)
        }
        return rows
    }
}
