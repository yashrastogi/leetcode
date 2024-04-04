class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var maxNum = -1, maxNumIndex = -1
        func binarySearch(_ lo: Int = 0, _ hi: Int = arr.count - 1) {
            guard lo <= hi else { return }
            let mid = (lo + hi) / 2

            if arr[mid] > maxNum {
                maxNum = arr[mid]
                maxNumIndex = mid
            }
            if arr[mid] > arr[mid + 1] {
                binarySearch(lo, mid - 1)
            } else {
                binarySearch(mid + 1, hi)
            }
        }
        binarySearch()
        return maxNumIndex
    }
}