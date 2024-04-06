class Solution {
  func search(_ nums: [Int], _ target: Int) -> Bool {
    func binarySearch(_ lo: Int = 0, _ hi: Int = nums.count - 1) -> Bool {
      guard lo <= hi else { return false }
      let mid = (lo + hi) / 2
      if nums[mid] == target {
        return true
      }
      if nums[mid] == nums[lo] && nums[mid] == nums[hi] {
        return binarySearch(lo + 1, hi - 1)
      }
      if nums[mid] >= nums[lo] && nums[mid] <= nums[hi] {
        if nums[mid] < target {
          return binarySearch(mid + 1, hi)
        } else {
          return binarySearch(lo, mid - 1)
        }
      } else {
        return binarySearch(lo, mid - 1) || binarySearch(mid + 1, hi)
      }
    }

    return binarySearch()
  }
}