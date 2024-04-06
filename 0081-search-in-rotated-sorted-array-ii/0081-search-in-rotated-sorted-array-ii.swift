class Solution {
  func search(_ nums: [Int], _ target: Int) -> Bool {
    var lo = 0, hi = nums.count - 1
    while lo <= hi {
      let mid = (lo + hi) / 2
      if nums[mid] == target {
        return true
      } else if nums[lo] == nums[mid] && mid != lo {
        lo += 1
      } else if nums[mid] == nums[hi] && hi != lo {
        hi -= 1
      } else if nums[lo] <= nums[mid] {
        // left half is sorted
        if target < nums[mid] && target >= nums[lo] {
          hi = mid - 1
        } else {
          lo = mid + 1
        }
      } else {
        // right half is sorted
        if target > nums[mid] && target <= nums[hi] {
          lo = mid + 1
        } else {
          hi = mid - 1
        }
      }
    }
    return false
  }
}