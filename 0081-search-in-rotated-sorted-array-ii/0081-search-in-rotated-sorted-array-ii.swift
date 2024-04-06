class Solution {
    func search(_ nums: [Int], _ target: Int) -> Bool {
        func findHighest(_ lo: Int = 0, _ hi: Int = nums.count - 1) -> Int {
            var maxNum = -Int.max, maxNumI = -1
            for i in lo ... hi {
                if nums[i] > maxNum {
                    maxNum = nums[i]
                    maxNumI = i
                }
            }
            return maxNumI
        }

        func binarySearch(_ startIndex: Int, _ lo: Int = 0, _ hi: Int = nums.count - 1) -> Bool {
            guard lo <= hi else { return false }
            let mid = (lo + hi) / 2
            let midIndex = (startIndex + mid) % nums.count
            if nums[midIndex] == target {
                return true
            } else if nums[midIndex] < target {
                return binarySearch(startIndex, mid + 1, hi)
            } else {
                return binarySearch(startIndex, lo, mid - 1)
            }
        }
        
        let startIndex = (findHighest() + 1) % nums.count
        return binarySearch(startIndex)
    }
}