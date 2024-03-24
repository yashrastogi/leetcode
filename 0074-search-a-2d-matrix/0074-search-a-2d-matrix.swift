class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        return binarySearch(matrix, target, 0, (matrix.count * matrix[0].count) - 1)
    }

    func indexMapper(_ i: Int, _ matrix: [[Int]]) -> [Int] {
        return [i / matrix[0].count, i % matrix[0].count]
    }

    func binarySearch(_ matrix: [[Int]], _ target: Int, _ lo: Int, _ hi: Int) -> Bool {
        if lo > hi { return false }
        let mid = (hi - lo) / 2 + lo
        let ix = indexMapper(mid, matrix)
        if matrix[ix[0]][ix[1]] == target {
            return true
        } else if matrix[ix[0]][ix[1]] < target {
            return binarySearch(matrix, target, mid + 1, hi)
        } else {
            return binarySearch(matrix, target, lo, mid - 1)
        }
    }
}