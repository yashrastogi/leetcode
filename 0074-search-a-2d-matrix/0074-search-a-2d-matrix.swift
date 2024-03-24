class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        var arr = [Int]()
        matrix.forEach { m in arr += m }
        return binarySearch(arr, target, 0, arr.count - 1)
    }

    func binarySearch(_ arr: [Int], _ target: Int, _ lo: Int, _ hi: Int) -> Bool {
        if lo > hi { return false }
        let mid = (hi - lo) / 2 + lo
        if arr[mid] == target {
            return true
        } else if arr[mid] < target {
            return binarySearch(arr, target, mid + 1, hi)
        } else {
            return binarySearch(arr, target, lo, mid - 1)
        }
    }
}