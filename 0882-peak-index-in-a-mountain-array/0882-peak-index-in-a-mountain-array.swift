class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var lo = 0, hi = arr.count - 1
        var mid = (lo + hi) / 2
        while lo <= hi {
            if arr[mid] > arr[mid + 1] {
                hi = mid - 1
            } else {
                lo = mid + 1
            }
            mid = (lo + hi) / 2
        }
        return lo
    }
}